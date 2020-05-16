if __name__ == '__main__':
    if args.apptype:
        tokenPath = Path('authToken.txt')
        if tokenPath.exists():
            tokenFile = tokenPath.open('r')
        else:
            tokenFile = tokenPath.open('w+')
        savedAuthToken = tokenFile.read().strip()
        authToken = savedAuthToken if savedAuthToken and not args.token else args.token
        idOrToken = authToken if authToken else args.email
        try:
            line = LINE(idOrToken, args.passwd, appType=args.apptype, systemName=args.systemname, channelId=args.channelid, showQr=args.showqr)
            tokenFile.close()
            tokenFile = tokenPath.open('w+')
            tokenFile.write(line.authToken)
            tokenFile.close()
        except TalkException as talk_error:
            if args.traceback: traceback.print_tb(talk_error.__traceback__)
            sys.exit('++ Error : %s' % talk_error.reason.replace('_', ' '))
        except Exception as error:
            if args.traceback: traceback.print_tb(error.__traceback__)
            sys.exit('++ Error : %s' % str(error))
    else:
        for appType in listAppType:
            tokenPath = Path('authToken.txt')
            if tokenPath.exists():
                tokenFile = tokenPath.open('r')
            else:
                tokenFile = tokenPath.open('w+')
            savedAuthToken = tokenFile.read().strip()
            authToken = savedAuthToken if savedAuthToken and not args.token else args.token
            idOrToken = authToken if authToken else args.email
            try:
                line = LINE(idOrToken, args.passwd, appType=appType, systemName=args.systemname, channelId=args.channelid, showQr=args.showqr)
                tokenFile.close()
                tokenFile = tokenPath.open('w+')
                tokenFile.write(line.authToken)
                tokenFile.close()
            except TalkException as talk_error:
                print ('++ Error : %s' % talk_error.reason.replace('_', ' '))
                if args.traceback: traceback.print_tb(talk_error.__traceback__)
                if talk_error.code == 1:
                    continue
                sys.exit(1)
            except Exception as error:
                print ('++ Error : %s' % str(error))
                if args.traceback: traceback.print_tb(error.__traceback__)
                sys.exit(1)

                eyJhbGciOiJSUzI1NiJ9.
                eyJpZCI6MTAwMDMsInVzZXJuYW1lIjoieW91Z3RhbyIsImV4cCI6NTMyMjExOTM3NX0
                eyJpZCI6MTAwMDAsInVzZXJuYW1lIjoieGlhb3J1aSIsImV4cCI6NTMwMjQ2NDEzNX0.
                fHGMfpZmnp8K0Ps2-gTYqfy8C6IEvu_MuxrEoAPR4E3zpo2oD_BVHVVHRtBQnDEZy7AgTj8X14qrWvjyLMJhvsJMrDf1YhhsmT15oJi9Ve-lf0W1ohnOfxY8dRkyOifn302DB7K6cpdbA8EsCR81vq3RE1wYbKPmq6sMVGeAOJ4