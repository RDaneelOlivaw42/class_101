# Class 101

Wrote a function to upload files to Dropbox (remote cloud storage).
<p>
Imported dropbox module.
<p>
Uploading files to dropbox -
<br>
 dbx = dropbox.Dropbox(<i>self.access_token</i>)
<br>
dbx.files_upload( <i>files_from</i>, <i>file_to</i> )

<p>
Self-access token generation -<br>
  1. Go to - https://www.dropbox.com/developers/apps<br>
  2. Create app<br>
  3. Give Permissions in Permissions Tab<br>
  4. Click on generate access token<br>
  5. Copy token generated
  
