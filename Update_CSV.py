#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time
import chilkat

while 1:

#  Important: It is helpful to send the contents of the
#  sftp.LastErrorText property when requesting support.

    sftp = chilkat.CkSFtp()
    success = sftp.UnlockComponent('MARQUE.CB1112018_qbN4VB2x10pV')

    if success != True:
        print sftp.lastErrorText()
        sys.exit()

#  Set some timeouts, in milliseconds:

    sftp.put_ConnectTimeoutMs(5000)
    sftp.put_IdleTimeoutMs(10000)

#  Connect to the SSH server.
#  The standard SSH port = 22
#  The hostname may be a hostname or IP address.

    hostname = "sftp://sftp.gdom.net"
    port = 22
    success = sftp.Connect(hostname,port)
    if success != True:
        print sftp.lastErrorText()
        sys.exit()

    success = sftp.AuthenticatePw('smellysocks', 'dai0xaeJ')
    if success != True:
        print sftp.lastErrorText()
        sys.exit()

#  After authenticating, the SFTP subsystem must be initialized:

    success = sftp.InitializeSftp()
    if success != True:
        print sftp.lastErrorText()
        sys.exit()

#  Open a file on the server:

    handle = sftp.openFile('Smelly_Socks_Database.csv', 'readOnly',
                           'openExisting')
    if sftp.get_LastMethodSuccess() != True:
        print sftp.lastErrorText()
        sys.exit()

#  Download the file:

    success = sftp.DownloadFile(handle,
                                "C:\Users\Colin\Documents\Data_Science\smellysocksproject1\smelly_socks_db.csv"
                                )
    if success != True:
        print sftp.lastErrorText()
        sys.exit()

#  Close the file.

    success = sftp.CloseHandle(handle)
    if success != True:
        print sftp.lastErrorText()
        sys.exit()

    print 'Success.'
    time.sleep(120)
