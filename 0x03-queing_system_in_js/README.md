# 0x03-queing\_system\_in\_js

This project is part of the **ALX Backend Specialization** and demonstrates how to implement a basic queuing system in **Node.js** using **Redis** and **Kue**. It includes job creation, processing, progress tracking, and error handling.

## 📦 Project Structure

* Uses **Redis** as the backend data store
* Uses **Kue** to manage job queues
* Demonstrates:

  * Seat reservation system using Redis
  * Job creation and queuing
  * Notification handling and progress reporting
  * Error handling with blacklisted phone numbers

## 🛠 Setup

1. **Clone the repository**:

   ```bash
   git clone <repo-url>
   cd 0x03-queing_system_in_js
   ```

2. **Install dependencies**:

   ```bash
   npm install
   ```

3. **Ensure Redis server is running** on your machine.

4. **Run a sample file**:

   ```bash
   node <filename>.js
   ```

## 📚 Dependencies

Run `npm list redis`:

```bash
queuing_system_in_js@1.0.0
├─┬ kue@0.11.6
│ ├── redis@2.6.5
│ └─┬ reds@0.2.5
│   └── redis@0.12.1
└── redis@3.1.2
```

> **Note:** Multiple versions of `redis` are installed due to Kue and Reds dependencies. The main app uses `redis@3.1.2`.

