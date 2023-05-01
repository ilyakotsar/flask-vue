# Flask - Vue

### Backend Setup

```
cd backend

python3 -m venv venv

. venv/bin/activate

pip install -r requirements.txt

flask db init

flask db migrate -m "Initial migration"

flask db upgrade

flask run
```

### Frontend Setup

```
cd frontend

npm install

npm run dev
```
