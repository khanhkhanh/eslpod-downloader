import os, sys, requests, getopt

"""Script that downloads episodes of ESL Podcast"""

def _main(argv):
    if len(argv[1:]) == 0:
        _get_help_and_exit()

    type_episode = None
    start_episode = None
    end_episode = None
    single_episode = None

    try:
        opts, args = getopt.getopt(argv, 'ht:s:e:o:', [])
    except getopt.GetoptError:
        _get_help_and_exit()

    for opt, args in opts:
        if opt == '-h':
            print get_help_message()
            sys.exit()
        elif opt in ('-t'):
            type_episode = args
        elif opt in ('-s'):
            start_episode = int(args)
        elif opt in ('-e'):
            end_episode = int(args)
        elif opt in ('-o'):
            single_episode = int(args)

    if type_episode in ('eslpod', 'cafe') is False:
        _get_help_and_exit()

    if start_episode is not None and end_episode is not None:
        if start_episode > end_episode:
            _get_help_and_exit()
        else:
            _download_episodes(type_episode, start_episode, end_episode)
    elif single_episode is not None:
        _download_episodes(type_episode, single_episode, single_episode)

def _get_help_and_exit():
    print '-t - type of podcast - "eslpod", "ec"'
    print '-s - start of range of episodes numbers to download'
    print '-e - end of range of episodes numbers to download'
    print '-o - single episode number to download'
    print 'python eslpod.py -t "eslpod" -s 1200 -e 1208'
    print 'python eslpod.py -t "eslpod" -o 1207'
    sys.exit(2)

def _download_episodes(ep_type=str, start=int, end=int):
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    cur_dir = os.path.join(cur_dir, ep_type)

    # Create dirs if does not exist
    if not os.path.exists(cur_dir):
        os.makedirs(cur_dir)

    base_url = 'http://libsyn.com/media/eslpod'

    for episode_number in xrange(start, end):
        file_name = ep_type + str(episode_number) + '.mp3'
        url = base_url + '/' + file_name
        print 'Downloading ' + file_name
        response = requests.get(url)
        file_path = os.path.join(cur_dir, file_name)
        with open(file_path, 'w') as fh:
            fh.write(response.content)

if __name__ == '__main__':
    _main(sys.argv[1:])
