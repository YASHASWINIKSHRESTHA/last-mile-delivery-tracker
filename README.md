# 📦 Last-Mile Delivery Confirmation System

**Spring Boot Backend + Streamlit UI**

---

## 📌 Project Description

This project implements a **Last-Mile Delivery Confirmation System** that securely verifies deliveries using a **Shipment ID and OTP-based confirmation mechanism**.

The system is designed following a **3-Tier Architecture** and focuses on **backend correctness, data integrity, and secure delivery validation**, as required by the assignment. A lightweight **Streamlit-based UI** is added on top of the backend to demonstrate real-time interaction, while **Postman** is used to verify and test API execution independently.

---

## 🧠 What Problem Does This Project Solve?

In logistics systems, the final delivery step (last mile) is prone to:

* Incorrect delivery confirmations
* Manual errors by delivery agents
* Lack of real-time verification
* No secure proof of delivery

This project solves these issues by:

* Enforcing **OTP-based delivery confirmation**
* Preventing **duplicate or fraudulent deliveries**
* Persisting delivery status in a **relational database**
* Exposing **REST APIs** for scalable integration

---

## 🏗️ System Architecture (3-Tier)

```
Presentation Tier
 ├── Streamlit UI (Delivery Agent Interface)
 └── Postman (API Testing & Verification)

Application Tier
 └── Spring Boot REST API
     ├── Business Logic
     ├── OTP Validation
     └── Shipment State Management

Data Tier
 └── MySQL Database
     └── Persistent Shipment Records
```

✔ Clear separation of concerns
✔ Backend-centric design
✔ UI is only a consumer, not logic holder

---

## ⚙️ Tech Stack

### Backend

* Java 17
* Spring Boot 4.x
* Spring Data JPA (Hibernate)
* RESTful APIs
* Maven

### Database

* MySQL 8.x

### Frontend / UI

* Python
* Streamlit

### Tools & Utilities

* IntelliJ IDEA
* Postman (API testing & validation)
* Git & GitHub

---

## 📂 Repository Structure

```
last-mile-delivery-tracker/
│
├── src/main/java/com/delivery/lastmile
│   ├── controller/
│   │   └── ShipmentController.java
│   ├── service/
│   │   └── ShipmentService.java
│   ├── repository/
│   │   └── ShipmentRepository.java
│   ├── entity/
│   │   └── Shipment.java
│   └── LastmileApplication.java
│
├── src/main/resources
│   └── application.properties
│
├── pom.xml
├── mvnw / mvnw.cmd
└── README.md
```

> The **Streamlit UI** is maintained in a separate repository and connects to this backend via REST APIs.

---

## 🗄️ Database Design

### `shipments` Table

| Column Name   | Type        | Description                      |
| ------------- | ----------- | -------------------------------- |
| id            | BIGINT (PK) | Internal auto-generated ID       |
| shipment_id   | VARCHAR     | Public tracking ID               |
| customer_name | VARCHAR     | Recipient name                   |
| otp_code      | VARCHAR     | OTP for delivery confirmation    |
| status        | ENUM        | PENDING / IN_TRANSIT / DELIVERED |
| delivered_at  | TIMESTAMP   | Delivery completion time         |
| delivered_by  | VARCHAR     | Delivery agent                   |

✔ Unique shipment IDs
✔ Prevents re-delivery
✔ Persistent state tracking

---

## 🔌 Backend API Endpoints

### 1️⃣ Track Shipment

**GET**

```
/api/shipments/{shipmentId}
```

**Sample Response**

```json
{
  "shipmentId": "SHIP1766914906941",
  "customerName": "John Doe",
  "status": "IN_TRANSIT"
}
```

---

### 2️⃣ Confirm Delivery Using OTP

**POST**

```
/api/shipments/{shipmentId}/deliver?otp=123456
```

**Business Rules**

* OTP must match
* Shipment must not already be DELIVERED
* Delivery timestamp is recorded

**Sample Response**

```json
{
  "status": "DELIVERED",
  "deliveredAt": "2025-01-01T12:30:45"
}
```

---

### 3️⃣ Create Shipment (Testing / Demo)

**POST**

```
/api/shipments/create?customerName=Alice
```

Used to generate test shipments for UI and Postman verification.

---

## 🧪 API Verification Using Postman

Postman was used to:

* Verify all API endpoints independently
* Validate OTP failure and success cases
* Ensure correct HTTP status codes
* Confirm database updates after delivery

✔ Screens tested before UI integration
✔ Ensures backend correctness

---

## 🖥️ Streamlit UI Integration

A **Streamlit-based frontend** was created to simulate a **delivery agent interface**.

### UI Features

* Input Shipment ID
* Input OTP
* Track shipment status
* Mark delivery as completed
* Clean UI with background image and styled components

The UI communicates with the backend using HTTP requests and **does not contain any business logic**.

---

## 🔐 Security & Data Integrity

* OTP validation enforced strictly on backend
* Delivered shipments cannot be re-processed
* Database constraints ensure consistency
* UI acts only as a client, not a decision maker

---

## 🚀 How to Run the Project Locally

### Backend Setup

1. Create database:

```sql
CREATE DATABASE last_mile_delivery;
```

2. Configure `application.properties`

3. Run backend:

```bash
./mvnw spring-boot:run
```

Backend runs at:

```
http://localhost:8080
```

---

### Streamlit UI Setup

```bash
pip install streamlit requests
streamlit run app.py
```

UI runs at:

```
http://localhost:8501
```

---

## 🤖 Use of AI (Disclosure)

AI tools were used responsibly to:

* Assist with debugging configuration issues
* Improve code structure and documentation
* Validate architectural decisions
* Enhance UI styling ideas

All **core logic, API design, and implementation decisions** were manually verified and implemented to ensure learning integrity.

---

## 📌 Assignment Alignment Checklist

✔ 3-Tier Architecture
✔ Backend-centric design
✔ RESTful APIs
✔ MySQL persistence
✔ OTP-based confirmation
✔ Postman API verification
✔ UI integration (optional enhancement)
✔ Detailed documentation

---

## 🔮 Future Enhancements

* Android mobile client
* OTP expiry & retry limits
* Authentication & role management
* Cloud deployment (Docker / AWS)
* Delivery analytics dashboard

---

## 👤 Author

**Yashaswini Kshrestha**
Backend Development | Java | Spring Boot | System Design

