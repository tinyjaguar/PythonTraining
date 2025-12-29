#!/bin/bash

echo "=== Doctor Appointment API Testing Workflow ==="
echo

# 1. Register a doctor
echo "1. Registering a doctor..."
DOCTOR_RESPONSE=$(curl -s -X POST "http://127.0.0.1:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"email": "doctor@test.com", "password": "password123", "name": "Dr. Smith", "role": "DOCTOR"}')

DOCTOR_ID=$(echo $DOCTOR_RESPONSE | jq -r '.id')
echo "Doctor registered with ID: $DOCTOR_ID"

# 2. Login as doctor
echo "2. Doctor login..."
LOGIN_RESPONSE=$(curl -s -X POST "http://127.0.0.1:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email": "doctor@test.com", "password": "password123"}')

DOCTOR_TOKEN=$(echo $LOGIN_RESPONSE | jq -r '.access_token')
echo "Doctor JWT token obtained"

# 3. Set doctor availability
echo "3. Setting doctor availability..."
AVAILABILITY_RESPONSE=$(curl -s -X POST "http://127.0.0.1:8000/doctors/availability" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DOCTOR_TOKEN" \
  -d '{"start_time": "2024-01-01T09:00:00", "end_time": "2024-01-01T17:00:00"}')

echo "Doctor availability set: $AVAILABILITY_RESPONSE"

# 4. Register a patient
echo "4. Registering a patient..."
PATIENT_RESPONSE=$(curl -s -X POST "http://127.0.0.1:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"email": "patient@test.com", "password": "password123", "name": "John Doe", "role": "PATIENT"}')

PATIENT_ID=$(echo $PATIENT_RESPONSE | jq -r '.id')
echo "Patient registered with ID: $PATIENT_ID"

# 5. Login as patient
echo "5. Patient login..."
PATIENT_LOGIN=$(curl -s -X POST "http://127.0.0.1:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email": "patient@test.com", "password": "password123"}')

PATIENT_TOKEN=$(echo $PATIENT_LOGIN | jq -r '.access_token')
echo "Patient JWT token obtained"

# 6. List doctors
echo "6. Listing all doctors..."
curl -s -X GET "http://127.0.0.1:8000/doctors" \
  -H "Authorization: Bearer $PATIENT_TOKEN" | jq '.'

# 7. Check doctor availability
echo "7. Checking doctor availability..."
curl -s -X GET "http://127.0.0.1:8000/doctors/$DOCTOR_ID/availability" \
  -H "Authorization: Bearer $PATIENT_TOKEN" | jq '.'

# 8. Book appointment
echo "8. Booking appointment..."
APPOINTMENT_RESPONSE=$(curl -s -X POST "http://127.0.0.1:8000/appointments" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $PATIENT_TOKEN" \
  -d "{\"doctor_id\": $DOCTOR_ID, \"start_time\": \"2024-01-01T10:00:00\", \"end_time\": \"2024-01-01T11:00:00\"}")

echo "Appointment booked: $APPOINTMENT_RESPONSE"

# 9. View appointments
echo "9. Viewing patient appointments..."
curl -s -X GET "http://127.0.0.1:8000/appointments" \
  -H "Authorization: Bearer $PATIENT_TOKEN" | jq '.'

# 10. View doctor appointments
echo "10. Viewing doctor appointments..."
curl -s -X GET "http://127.0.0.1:8000/appointments" \
  -H "Authorization: Bearer $DOCTOR_TOKEN" | jq '.'

echo
echo "=== Testing Complete ==="
