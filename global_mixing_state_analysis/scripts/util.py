import xarray as xr
import cartopy
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib
import numpy as np
import cartopy.crs as ccrs

def plot_difference_EqualEarth(var,DJF_mask,JJA_mask):
    """
    Plot the 1 x 3 figures using EqualEarth projection
    """
    fig = plt.figure(figsize=(16,4))
    ax1 = plt.subplot(131,projection=ccrs.EqualEarth());
    im1=DJF_mask[var].plot(ax=ax1,transform=ccrs.PlateCarree(),
                           vmax=100,vmin=0,add_colorbar=False)
    ax1.coastlines()
    plt.colorbar(im1, orientation="horizontal", pad=0.15)
    #plt.show()

    ax2 = plt.subplot(132,projection=ccrs.EqualEarth());
    im2=JJA_mask[var].plot(ax=ax2,transform=ccrs.PlateCarree(),
                           vmax=100,vmin=0,add_colorbar=False)
    a2.coastlines()
    plt.colorbar(im2, orientation="horizontal", pad=0.15)
    #plt.show()

    DJF_minus_JJA=DJF_mask[var]-JJA_mask[var]
    ax3 = plt.subplot(133,projection=ccrs.EqualEarth());
    im3=DJF_minus_JJA.plot(ax=ax3,transform=ccrs.PlateCarree(),add_colorbar=False)
    plt.colorbar(im3, orientation="horizontal", pad=0.15)
    plt.show()
    
def plot_difference(var,DJF_mask,JJA_mask):
    """
    Plot the 1 x 3 figures without projection
    """
    fig = plt.figure(figsize=(16,4))
    ax1 = plt.subplot(131,projection=ccrs.PlateCarree());
    im1=DJF_mask[var].plot(ax=ax1,
                           vmax=100,vmin=0,add_colorbar=False)
    ax1.coastlines()
    plt.colorbar(im1, orientation="horizontal", pad=0.15)

    ax2 = plt.subplot(132,projection=ccrs.PlateCarree());
    im2=JJA_mask[var].plot(ax=ax2,
                           vmax=100,vmin=0,add_colorbar=False)
    plt.colorbar(im2, orientation="horizontal", pad=0.15)
    ax2.coastlines()

    DJF_minus_JJA=DJF_mask[var]-JJA_mask[var]
    ax3 = plt.subplot(133,projection=ccrs.PlateCarree());
    im3=DJF_minus_JJA.plot(ax=ax3,add_colorbar=False)
    plt.colorbar(im3, orientation="horizontal", pad=0.15)
    ax3.coastlines()
    plt.show()
    
def plot_difference_with_anchor(var,DJF_mask,JJA_mask,lat_min, lat_max, lon_min, lon_max):
    """
    Plot the 1 x 3 figures using anchor
    """
    fig = plt.figure(figsize=(16,4))
    ax1 = plt.subplot(131,projection=ccrs.PlateCarree());
    im1=DJF_mask[var].plot(ax=ax1,
                           vmax=100,vmin=0,add_colorbar=False,cmap='RdYlBu_r')
    ax1.add_patch(mpatches.Rectangle(xy=[lon_min, lat_min], 
                                     width=(lon_max-lon_min), 
                                     height=(lat_max-lat_min),
                                 edgecolor="black",
                                 facecolor='None',
                                 lw=1.5))
    ax1.coastlines(alpha=0.66)
    plt.colorbar(im1, orientation="horizontal", pad=0.15)
    #plt.show()

    ax2 = plt.subplot(132,projection=ccrs.PlateCarree());
    im2=JJA_mask[var].plot(ax=ax2,
                           vmax=100,vmin=0,add_colorbar=False,cmap='RdYlBu_r')
    ax2.add_patch(mpatches.Rectangle(xy=[lon_min, lat_min], 
                                     width=(lon_max-lon_min), 
                                     height=(lat_max-lat_min),
                                 edgecolor="black",
                                 facecolor='None',
                                 lw=1.5))
    ax2.coastlines(alpha=0.66)
    plt.colorbar(im2, orientation="horizontal", pad=0.15)
    #plt.show()

    DJF_minus_JJA=DJF_mask[var]-JJA_mask[var]
    ax3 = plt.subplot(133,projection=ccrs.PlateCarree());
    im3=DJF_minus_JJA.plot(ax=ax3,add_colorbar=False)
    ax3.add_patch(mpatches.Rectangle(xy=[lon_min, lat_min], 
                                     width=(lon_max-lon_min), 
                                     height=(lat_max-lat_min),
                                 edgecolor="black",
                                 facecolor='None',
                                 lw=2.5))
    ax3.coastlines(alpha=0.66)
    plt.colorbar(im3, orientation="horizontal", pad=0.15)
    plt.show()

def select_data(ds, lat_min, lat_max, lon_min, lon_max):
    """
    select the dataset given the box information
    """
    ds_select = ds.where((ds.lat>lat_min)&(ds.lat<lat_max)
                        & (ds.lon>lon_min) & (ds.lon<lon_max))
    return ds_select

def plot_select_diff(ds1, ds2, lat_min, lat_max, lon_min, lon_max):
    """
    Plot the difference between dataset given the box information
    """
    diff = ds1-ds2
    area_select = select_data(diff, lat_min, lat_max, lon_min, lon_max)
    return area_select

def plot_select_bar(ds, lat_min, lat_max, lon_min, lon_max, verbose=None):
    """
    Plot the distribution
    """
    var_ls = ["bc_per","dst_per","pom_per","ncl_per","soa_per","so4_per"]
    var_ls_all = var_ls + ["opt1_per","hyg_per"]
    df=select_data(ds, lat_min, lat_max, lon_min, lon_max).to_dataframe()\
    .reset_index()
    df[var_ls_all] = df[var_ls_all]*100
    df["opt1_per_"] = 100-df["opt1_per"]
    df["hyg_per_"] = 100-df["hyg_per"]
    
    aero=df[var_ls+["chi_abd"]].dropna().mean(axis=0)
    surro_opt=df[["opt1_per","opt1_per_","chi_opt1"]].rename({
        "opt1_per":"bc",
        "opt1_per_":"non-bc"
    }).dropna().mean(axis=0)
    """
        ds["s1_hyg"] = ds["Mass_bc"] + ds["Mass_dst"] + ds["Mass_pom"]
        ds["hyg_per"] = ds["s1_hyg"]/(ds["s1_hyg"]+ds["s2_hyg"])
    """
    surro_hyg=df[["hyg_per","hyg_per_","chi_hyg"]].rename({
        "hyg_per_":"hygroscopic",
        "hyg_per":"nonhygro"
    }).dropna().mean(axis=0)

    f, ((ax1,ax2,ax3)) = plt.subplots(1,3,figsize=(12,3.5))
    aero.plot.bar(ax=ax1)
    ax1.set_ylim(0,100)
    surro_opt.plot.bar(ax=ax2)
    ax2.set_ylim(0,100)
    surro_hyg.plot.bar(ax=ax3)
    ax3.set_ylim(0,100)
    plt.show()
    
    if verbose != None:
        print(aero)
        print(surro_opt)
        print(surro_hyg)
    return aero