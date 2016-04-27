# scripts
#
## A set of scripts to rename, move and manage series in plex.
It can copy (link) pending files in a folder (those with 1 link only) to another folder
It can try to guess and rename the files in a plex-friendly name
You can supply your own arguments to the renamer (or copy since it passes args to renamer) 
like:
  -s{season_number} (nice to convert s1e01 to s01e01
  -d Replaces dots on name with spaces
  -k Don't delete double spaces in the file name
  -t Capitalize each letter of series name title
  etc.

See the scripts for additional info

The second script (2.py) allows for custom regex grouping patterns. Use it at your own risk!
