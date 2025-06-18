import createPushNotificationsJobs from "./8-job";
import { expect } from 'chai';

const kue = require(('kue'))

, queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  before(() => queue.testMode.enter());
  afterEach(() => queue.testMode.clear());
  after(() => queue.testMode.exit());

    it('display a error message if jobs is not an array', () => {
      expect(() => createPushNotificationsJobs('job1', queue).to.throw('Jobs is not an array'))
    })

    it('create two new jobs to the queue', () => {
      const jobs = [
        { phoneNumber: '1234567890', message: 'Hello' },
        { phoneNumber: '0987654321', message: 'World' },
      ];
      createPushNotificationsJobs( jobs, queue );
      expect(queue.testMode.jobs.length).to.equal(2);
      expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
      expect(queue.testMode.jobs[1].data.message).to.equal('World');
    })

})