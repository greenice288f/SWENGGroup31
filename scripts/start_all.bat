cd ..
ECHO "Installing Backend Dependencies..."
cd backend
python3 -m pip install -r requirements.txt
cd ..
ECHO "Installing Frontend Dependencies"
cd frontend/my-app
call npm install
cd ../..
ECHO "Starting Backend..."
cd backend
start "Backend" call "python3" "server.py"
cd ..
ECHO "Starting Frontend..."
cd frontend/my-app
start "Frontend" npm start

