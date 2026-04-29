# HR-Recruitment-Process-Form
A portal where HR can add/track/update the recruitment process of a candidate.

## Deploying on Vercel

This project is now set up to use Vercel's zero-config Django support.

### Environment variables

Add these in your Vercel project settings:

- `SECRET_KEY`: any long random Django secret
- `DATABASE_URL`: a hosted Postgres connection string if you want persistent production data
- `ALLOWED_HOSTS`: optional comma-separated custom domains
- `DEBUG`: keep this unset or set it to `False` in production

### Important note about uploads

The app can deploy on Vercel, but Vercel's filesystem is ephemeral. That means uploaded files like resumes and aadhar documents won't persist unless you connect external storage such as Vercel Blob, S3, or another file store.

### Deployment steps

1. Import this repository into Vercel.
2. Set the environment variables above.
3. Deploy without adding a custom `vercel.json`.
4. Run migrations against your production database.

![Screenshot 2023-05-27 at 11 26 41 PM](https://github.com/adit098/HR-Recruitment-Process-Form/assets/54178152/a7f1e58c-c439-4172-9661-11f5e5344a45)
![Screenshot 2023-05-27 at 11 26 46 PM](https://github.com/adit098/HR-Recruitment-Process-Form/assets/54178152/3d958493-b63f-48d7-ad57-b28548f7420c)
![Screenshot 2023-05-27 at 11 27 07 PM](https://github.com/adit098/HR-Recruitment-Process-Form/assets/54178152/dc193d44-5f2e-49b3-be4e-79fa2f6bfa4a)
![Screenshot 2023-05-27 at 11 27 17 PM](https://github.com/adit098/HR-Recruitment-Process-Form/assets/54178152/90be6f65-2e8d-41f1-bc66-bac1a2636bef)
![Screenshot 2023-05-27 at 11 27 54 PM](https://github.com/adit098/HR-Recruitment-Process-Form/assets/54178152/faae6c23-65d6-414d-a895-a85f6e668274)
![Screenshot 2023-05-27 at 11 28 08 PM](https://github.com/adit098/HR-Recruitment-Process-Form/assets/54178152/7cf64af3-9815-40e2-84e6-596e977017f0)
![Screenshot 2023-05-27 at 11 29 06 PM](https://github.com/adit098/HR-Recruitment-Process-Form/assets/54178152/c4213f63-1c42-461e-b964-ba82949d3c80)
![Screenshot 2023-05-27 at 11 29 21 PM](https://github.com/adit098/HR-Recruitment-Process-Form/assets/54178152/6c21c8c9-5e01-4322-9fb9-72e96c6eb8d2)
![Screenshot 2023-05-27 at 11 30 05 PM](https://github.com/adit098/HR-Recruitment-Process-Form/assets/54178152/2c5d6f2b-7083-4d5f-8e40-97d78c23e2e2)
![Screenshot 2023-05-27 at 11 30 42 PM](https://github.com/adit098/HR-Recruitment-Process-Form/assets/54178152/8285b43b-e323-4cfb-9659-c61a57e2f67f)
![Screenshot 2023-05-27 at 11 30 53 PM](https://github.com/adit098/HR-Recruitment-Process-Form/assets/54178152/be37e3ba-386e-4dd7-afd3-ff5e0477019c)
![Screenshot 2023-05-27 at 11 31 04 PM](https://github.com/adit098/HR-Recruitment-Process-Form/assets/54178152/553b9d6b-37d9-40d7-b63f-13e5248a6dcc)
![Screenshot 2023-05-27 at 11 34 59 PM](https://github.com/adit098/HR-Recruitment-Process-Form/assets/54178152/c97226d5-d263-4dc7-b9f0-4ef6b2d496a6)
![Screenshot 2023-05-27 at 11 31 15 PM](https://github.com/adit098/HR-Recruitment-Process-Form/assets/54178152/ffe1a0b5-7174-4bcd-8149-65dd7bd3f40a)
![Screenshot 2023-05-27 at 11 31 33 PM](https://github.com/adit098/HR-Recruitment-Process-Form/assets/54178152/08b7be74-638e-4df9-85da-8b9bed74321b)

![Screenshot 2023-05-27 at 11 33 05 PM](https://github.com/adit098/HR-Recruitment-Process-Form/assets/54178152/5a870102-6452-4f0e-aab4-58ed742e514d)

![Screenshot 2023-05-27 at 11 33 40 PM](https://github.com/adit098/HR-Recruitment-Process-Form/assets/54178152/46712f2b-c4a9-40fe-9e6f-e853aef2de94)





