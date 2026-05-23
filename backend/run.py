import uvicorn
import os

if __name__ == "__main__":
    print("Starting Government Accident Detection & Alert System Backend...")
    # Run the uvicorn development server
    uvicorn.run(
        "app.main:app", 
        host="127.0.0.1", 
        port=8000, 
        reload=True
    )
