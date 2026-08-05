DB_PASSWORD = hunter2-concurrency

def connect():
    return fdb://user:{DB_PASSWORD}@localhost
