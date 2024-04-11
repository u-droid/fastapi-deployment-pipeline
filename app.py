"""
Code to test Continuous Integration using Github Actions
"""
import time

def app():
    """Test App"""
    print("App is running")
    time.sleep(2)
    print("App execution is completed")
    return True

if __name__=="__main__":
    assert app() is True
