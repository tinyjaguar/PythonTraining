"""
User Management System
Assignment: Object Modeling, OOP, Decorators, Generators, Special Methods
Single-file implementation covering Q1 to Q10.
"""

from collections import namedtuple
from datetime import datetime
import functools
import time

# ==========================================================
# Q4 & Q9: Decorators
# ==========================================================

def log_execution(enabled=True):
    """Logs function execution metadata if enabled."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if enabled:
                print(f"[LOG] Executing {func.__name__} at {datetime.now()}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


def execution_timer(func):
    """Measures execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] {func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


def requires_admin(func):
    """Ensures method can be executed only by admin users."""
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.get_role() != "ADMIN":
            raise PermissionError("Admin access required")
        return func(self, *args, **kwargs)
    return wrapper


# ==========================================================
# Q6: Immutable Configuration (namedtuple)
# ==========================================================

SystemConfig = namedtuple("SystemConfig", ["application", "version", "created_at"])


# ==========================================================
# Q1: Base Class and Inheritance
# ==========================================================

class User:
    active_users = 0

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        User.active_users += 1

    def get_role(self):
        return "GENERIC"

    def access_level(self):
        return "LIMITED"

    def deactivate(self):
        User.active_users -= 1

    # ======================================================
    # Q3: Special Methods
    # ======================================================

    def __str__(self):
        return f"User(name={self.name}, role={self.get_role()})"

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.user_id}, name='{self.name}')"

    def __len__(self):
        return len(self.name)

    def __eq__(self, other):
        return self.user_id == other.user_id

    def __lt__(self, other):
        return self.user_id < other.user_id

    def __call__(self):
        return f"{self.name} is logged in as {self.get_role()}"


class AdminUser(User):

    def get_role(self):
        return "ADMIN"

    def access_level(self):
        return "FULL"

    @requires_admin
    def shutdown_system(self):
        return "System shutdown initiated"


class CustomerUser(User):

    def get_role(self):
        return "CUSTOMER"

    def access_level(self):
        return "READ_ONLY"


# ==========================================================
# Q2: Classmethod and Staticmethod
# ==========================================================

class UserFactory:

    @classmethod
    def from_serialized(cls, data):
        """
        Create user from serialized string.
        Format: ROLE|ID|NAME
        """
        role, user_id, name = data.split("|")
        user_id = int(user_id)

        if role == "ADMIN":
            return AdminUser(user_id, name)
        elif role == "CUSTOMER":
            return CustomerUser(user_id, name)
        return User(user_id, name)

    @staticmethod
    def validate_username(name):
        """Validate username independently of class state."""
        return name.isalpha() and len(name) >= 3


# ==========================================================
# Q5: Generator-Based Data Streaming
# ==========================================================

class UserRepository:

    def __init__(self, users):
        self.users = users

    def stream_users(self):
        for user in self.users:
            yield user


# ==========================================================
# Q7: Loop-Else Control Flow
# ==========================================================

def find_user(users, name):
    for user in users:
        if user.name == name:
            return user
    else:
        print("User not found")
        return None


# ==========================================================
# Q8 & Q10: Execution Boundary and Integration
# ==========================================================

def main():
    config = SystemConfig(
        application="User Management System",
        version="1.0",
        created_at=datetime.now()
    )

    print(f"{config.application} v{config.version}")
    print(f"Started at: {config.created_at}\n")

    users = [
        UserFactory.from_serialized("ADMIN|1|Alice"),
        UserFactory.from_serialized("CUSTOMER|2|Bob"),
        UserFactory.from_serialized("CUSTOMER|3|Charlie")
    ]

    print(f"Active users: {User.active_users}\n")

    print(str(users[0]))
    print(repr(users[1]))
    print(f"Username length: {len(users[2])}")
    print(users[0]())

    repository = UserRepository(users)
    for user in repository.stream_users():
        print(f"Streaming user: {user.name}")

    find_user(users, "David")

    @log_execution(enabled=True)
    @execution_timer
    def sample_task():
        time.sleep(0.2)
        print("Task completed")

    sample_task()

    try:
        print(users[0].shutdown_system())
    except PermissionError as error:
        print(error)

    print(f"\nFinal active users count: {User.active_users}")


if __name__ == "__main__":
    main()
