#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import xmltodict
import click

from ConfigParser import SafeConfigParser


def get_config(key):
  """ Fetch config from config file """
  parser = SafeConfigParser()
  parser.read('.config')
  return parser.get(key)

class Match(object):
  """ Represents a cricinfo match """
  
  def __init__(self, title, link, description, guid):
      self.title = title
      self.link = link
      self.description = description
      self.guid = guid
  
  @classmethod
  def from_xml(self, xml):
      item = xmltodict.parse(xml)['item']
      return Match(item['title'], item['link'], item['description'], item['guid'])
      
  def __repr__(self):
      return '<Match=%s>'%self.title

def get_matches():
   """Fetches matches from the cricinfo url"""

   r = requests.get(parser.get('url'))
   soup = BeautifulSoup(r.text)
   for match in soup.find_all('item'):
    yield Match.from_xml(str(match))
    
def print_matches(matches):
  """Prints all matches to the console."""

  click.echo()
  for match in matches:
    click.secho('%s\t' % match.title, bold=True, fg="red", nl=False)
    click.echo()

@click.command()
def main():
  """A cli to Cricinfo to see live scores"""
  
  # fetch matches
  matches = get_matches()
  # print matches
  print_matches(matches)

if __name__ == '__main__':
  main()
