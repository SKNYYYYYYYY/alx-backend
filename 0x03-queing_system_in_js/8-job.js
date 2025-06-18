
export default function createPushNotificationsJobs(jobs, queue) {
  if (typeof(jobs) != 'object') {
    return (new Error('Jobs is not an array'))
  }
  for (let job_data of jobs) {
    let job = queue.create('push_notification_code_3', job_data);
    if (!queue.testMode) {
    job.save((err) => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`)
      }
    })
  } else {
    console.log(`Notification job created:`)
    job.save()
  }
    job.on('completed', () => console.log(`Notification job ${job.id} completed`))
    job.on('failed', (err) => console.log(`Notification job ${job.id} failed: ${err}`))
    job.on('progress', (progress) => console.log(`Notification job ${job.id} ${progress}% complete`))
  }
}
