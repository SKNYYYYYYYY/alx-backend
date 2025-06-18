const kue = require('kue')

, queue = kue.createQueue();

const job_data = {
  phoneNumber: String,
  message: String,
}

const job = queue.create('push_notification_code', job_data)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`)
    } else {
      console.log('Notification job failed')
    }
  })
  .on('completed', (result) => {
    console.log('Notification job completed')
  })