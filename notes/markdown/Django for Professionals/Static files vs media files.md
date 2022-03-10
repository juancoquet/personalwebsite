Note Type: #litnote
Source: [[📖 Django for Professionals]] ch12 p175

---
# Static files vs media files
The difference between static files and medial files is that static files are internal and developer-controlled, whereas media files are uploaded by users. This means that we can trust static files, but we definitely cannot trust media files as users could upload malware files.

Because of this, it is important to validate all uploaded files to ensure that they are what they claim to be, and not malware designed to attack our site.