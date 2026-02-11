def admin_only(dashboard):
    def wrapper(username):
        if username == "admin":
            dashboard(username)
        else:
            print("Access Denied")
    return wrapper


@admin_only
def dashboard(username):
    print("Welcome to Admin Dashboard")


dashboard("admin")
dashboard("user")
