# howto

### Create a .lazy file
1. Create an hdf5 file (example.lazy) from the iaea Live Chart of Nuclides (https://www-nds.iaea.org/relnsd/vcharthtml/VChartHTML.html)
   ```
   $ extractNuchart.py -p /location/of_the/output_file -n outputfile_name -c config_file 
   ```
   ```
   $ extractNuchart.py -p /home/user/Desktop -n dummy -c /home/user/Desktop/lazyspectra/config/nuchart.cfg -not "This is an example" 
   ```

   **default parameters:** --note ('')
