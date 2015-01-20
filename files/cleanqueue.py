#!/usr/bin/python

from deluge.ui.client import client
from twisted.internet import reactor, defer
from deluge.log import setupLogger
setupLogger()

RATIO_LIMIT = 10
SEED_LIMIT  = 1296000

def end_session(result):
  client.disconnect()
  reactor.stop()

def on_torrents_status(result):
  task_list = []
  for torrent_id, torrent_info in result.items():
    if float(torrent_info['ratio']) >= float(RATIO_LIMIT) or int(torrent_info['seeding_time']) >= int(SEED_LIMIT):
      print 'Removing expired torrent %s [id:%s]' %(torrent_info['name'], torrent_id)
      task_list.append(client.core.remove_torrent(torrent_id, True))
  defer.DeferredList(task_list).addCallback(end_session)

def on_session_state(result):
  client.core.get_torrents_status({'id': result}, ['name', 'ratio', 'seeding_time']).addCallback(on_torrents_status)

def on_connect_success(result):
  client.core.get_session_state().addCallback(on_session_state)

def on_connect_fail(result):
  print 'Connection failed!'

d = client.connect(username='deluge', password='deluge')
d.addCallback(on_connect_success)
d.addErrback(on_connect_fail)

reactor.run()
