npm install
electron-packager . Notification-app --overwrite --asar=true --platform=win32 --arch=ia32 --icon=icons/win/pea_image.ico --prune=true --out=release-builds --version-string.CompanyName=CE --version-string.FileDescription=CE --version-string.ProductName="notification app"
echo "packaged successfully and dumped into release-builds folder"