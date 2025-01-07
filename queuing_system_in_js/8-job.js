export default function createPushNotificationsJobs(jobs, queue) {
    if(!Array.isArray(jobs)) {
        return done (Error ('Jobs is not an array'))
    }

    jobs.forEach((j) => {
        let job = queue.create('push_notification_code_3', j)
        .save((err) => {
            if (!err) {
                console.log(`Notification job created: ${job.id}`);
            }
        });
    
        job.on('complete', () => {
            console.log(`Notification job ${job.id} completed`);
        });
    
        job.on('failed', (err) => {
            console.log(`Notification job ${job.id} failed: ${err}`);
        });
    
        job.on('progress', (progress) => {
            console.log(`Notification job ${job.id} ${progress}% complete`);
        });
    });

};
