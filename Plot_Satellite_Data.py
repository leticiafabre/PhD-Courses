#!/usr/bin/env python
# coding: utf-8

# In[1]:

# This code load satellite data in netcdf format and plot using cartpy

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import xarray as xr
import netCDF4 as nc
import cmocean
import cartopy
import cartopy.crs as ccrs
from cartopy.mpl.geoaxes import GeoAxes
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Load data
arq='RSS_AMSR2_ocean_L3_monthly_2022-01_v08.2.nc'
arq_data=nc.Dataset(arq)


# In[13]:


#to see the metadate if necessary
#print(arq_data)



# In[5]:


# Open .nc data and save as local variables
lat= arq_data['lat'][:]
lon= arq_data['lon'][:]
rain_rate= arq_data['rain_rate'][:]


# In[25]:


# Plotting with cartopy

#Define colormap
cmap = cmocean.cm.thermal

fig = plt.figure(figsize=(12,7))

#Define map projection and extentention
plain_crs = ccrs.PlateCarree()
ax1 = fig.add_subplot(1,1,1,projection=plain_crs)
ax1.set_extent([-60, -25,-5, 15], crs=ccrs.PlateCarree())

#Plot
p1= ax1.contourf(lon,lat,rain_rate,np.arange(0,1.5,0.1),cmap=cmap,zorder=1)


#Set colorbar properties
cbar = plt.colorbar(p1, fraction=0.04, pad=.05,extend='min',ax= ax1)
cbar.set_label('[mm/hr]', fontsize=10);
cbar.ax.tick_params(labelsize=10);

#Set axis properties
ax1.set_xticks(np.linspace(-60, -25, 5), crs=plain_crs)
ax1.set_yticks(np.linspace(-5, 15, 5), crs=plain_crs)
lon_formatter = LongitudeFormatter(zero_direction_label=True)
lat_formatter = LatitudeFormatter()
ax1.xaxis.set_major_formatter(lon_formatter)
ax1.yaxis.set_major_formatter(lat_formatter)

#Add coastiline
ax1.coastlines(zorder=4)
ax1.add_feature(cartopy.feature.LAND,zorder=3)

#Add labels and title
ax1.set_xlabel('Longitude',fontsize=12)
ax1.set_ylabel('Latitude',fontsize=12)
ax1.set_title('Sea-Surface Rain Rate', fontsize=14) 

#Save figure
plt.savefig('rain_rate', dpi=150, facecolor='w', edgecolor='w',
        orientation='portrait', format=None,
        transparent=False, bbox_inches='tight', pad_inches=0.1,
        metadata=None)


# In[ ]:




