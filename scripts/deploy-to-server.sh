#!/bin/sh

cd frontend/my-app
npm run build
scp -r build richardblazek.com:SWENGGroup31/frontend

cd ../..
scp -r backend richardblazek.com:SWENGGroup31

ssh richardblazek.com "sudo systemctl restart nginx sweng"
