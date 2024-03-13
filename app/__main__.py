""" Main module for running the application.
"""
import uvicorn

def main():
    """ Main function for running the application.
    """
    uvicorn.run("app:create_app", factory=True)


if __name__ == "__main__":
    main()
