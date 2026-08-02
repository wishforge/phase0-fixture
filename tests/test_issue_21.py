import importlib.util
import unittest

_HAVE = importlib.util.find_spec("fixturelib.issue_21") is not None


@unittest.skipUnless(_HAVE, "fixturelib/issue_21.py not implemented")
class Issue21Tests(unittest.TestCase):
    def test_cases(self):
        from fixturelib.issue_21 import retry_policy, run_planning_stage

        self.assertEqual(retry_policy(3), [300.0, 900.0, 2700.0])
        self.assertEqual(retry_policy(1), [300.0])
        self.assertEqual(retry_policy(0), [])
        self.assertEqual(
            retry_policy(5), [300.0, 900.0, 2700.0, 3600.0, 3600.0]
        )
        self.assertEqual(
            retry_policy(3, base_delay=10, factor=2, max_delay=25),
            [10.0, 20.0, 25.0],
        )
        self.assertTrue(all(isinstance(d, float) for d in retry_policy(4)))
        for bad in (
            dict(attempts=-1),
            dict(attempts="3"),
            dict(attempts=True),
            dict(attempts=2, base_delay=0),
            dict(attempts=2, factor=-1),
            dict(attempts=2, max_delay=0),
        ):
            with self.assertRaises(ValueError):
                retry_policy(**bad)

        result = run_planning_stage(["extract", "plan"])
        self.assertEqual(
            result,
            {
                "status": "ok",
                "attempts": 2,
                "completed": ["extract", "plan"],
                "schedule": [],
            },
        )

        flaky_once = lambda step, attempt: step == "extract" and attempt == 1
        result = run_planning_stage(["extract", "plan"], flaky=flaky_once)
        self.assertEqual(
            result,
            {
                "status": "ok",
                "attempts": 3,
                "completed": ["extract", "plan"],
                "schedule": [300.0],
            },
        )

        result = run_planning_stage(
            ["extract"], flaky=lambda step, attempt: True, policy=[1.0, 2.0]
        )
        self.assertEqual(
            result,
            {
                "status": "failed",
                "attempts": 3,
                "completed": [],
                "schedule": [1.0, 2.0],
            },
        )

        result = run_planning_stage(
            ["a", "b", "c"],
            flaky=lambda step, attempt: step == "b",
            policy=[5.0],
        )
        self.assertEqual(
            result,
            {
                "status": "failed",
                "attempts": 3,
                "completed": ["a"],
                "schedule": [5.0],
            },
        )

        self.assertEqual(
            run_planning_stage([]),
            {"status": "ok", "attempts": 0, "completed": [], "schedule": []},
        )
        for bad in (
            dict(steps="ab"),
            dict(steps=[1, 2]),
            dict(steps=["a"], flaky="nope"),
            dict(steps=["a"], policy=[-1.0]),
            dict(steps=["a"], policy="300"),
        ):
            with self.assertRaises(ValueError):
                run_planning_stage(**bad)
