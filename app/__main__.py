""" Main module for running the application.
"""
import uvicorn

def main():
    """ Main function for running the application.
    """
    uvicorn.run("app:create_app", host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
