const kue = require('kue')

const queue = kue.createQueue()

queue.process('email', (job, done) => {
  job.log('processing: ', job.data.title)
  setTimeout(() => {
    console.log('Finished processin (too late)');
    done();
  }, 6000 )
})
