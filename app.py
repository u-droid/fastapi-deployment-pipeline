"""
Code to test Continuous Integration using Github Actions
"""
import time

def app():
    try:
        """Test App"""
        print("App is running")
        time.sleep(5)
        print("App execution is completed")
        return True
    except Exception as e:
        return False

if __name__=="__main__":
    assert app()==True
