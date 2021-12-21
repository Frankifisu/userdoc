.. _AdvancedAMSview: 

Visualization of densities, orbitals potentials, ...
****************************************************

The AMSview module has many features. The basic use of AMSview is explained in the :ref:`first tutorial <GO_ETHANOL>`. 

In this tutorial some additional features of the AMSview module   are demonstrated. As a toy molecule the anthracene molecule is   used: 

Step 1: Get Single-Point calculation results with ADF on Anthracene
===================================================================

.. rst-class:: steps

  \ 
    | Start AMSinput
    | Set up an anthracene molecule (e.g. seach for 'anthracene' in the search box |Search| and select the 'Anthracene (ADF)' molecule)
    | Run the calculation with all default settings
    | When the calculation is ready, open AMSview

.. image:: /Images/VisualizationOfDensitiesEtc/t14-anthracene-view.png

Step 2: Details: Divergent and Rainbow Colormap, scalar range of   field on isosurface
======================================================================================

Now lets generate an isosurface of the density colored by the   electrostatic potential: 

.. rst-class:: steps

  \ 
    | **Add → Isosurface: Colored**
    | Left field selector at bottom: **Density → SCF**
    | Right field selector at bottom: **Potential → Coulomb Potential SCF**

.. image:: /Images/VisualizationOfDensitiesEtc/t14-anthracene-isosurface.png

The image is not as smooth as it could be, as a result   of the coarse grid used to calculate the density and potential.   So improve it by using a better grid: 

.. rst-class:: steps

  \ 
    | **Fields → Grid → Medium**
    | Click Yes to recalculate the 2 fields 
    | Play around with the isovalue, and note how the two numbers on the right change

When you change the iso value, the default range for the coloring   scheme will be adjusted automatically (provided you have not   changed them yourself). This range corresponds to the minimum and   maximum value of the coloring field (in this case the SCF   Potential) across the isosurface (in this case of the SCF   Density), at the isovalue you specify. 

Many more details can be set. First, begin by showing the color   legend: 

.. rst-class:: steps

  \ 
    | Check the Bar check box at the bottom right
    | (note: on some systems the text Bar might be partially invisible due to a resize box)
    | Click once in the color bar

.. image:: /Images/VisualizationOfDensitiesEtc/t14-anthracene-controls.png

The color bar shows the mapping of the colors used to the scalar   values of the potential. By clicking on the color bar you open   the detail settings, three extra lines with extra controls.   Another way to open the details line is using the pull-down menu   located on the left, currently with title "Isosurface: Colored".   In that menu you will find a "Show Details" and a "Hide Details"   command. If you have the color bar visible, you can also just   click on it to toggle the detailed controls. 

The first line of the detailed controls allows you to set what   the surface looks like: opacity, diffuse, specular and power.   Roughly speaking these control how shining or dull the surface   looks like, they are called the material properties controls. Additionally, there is the option to change the method to interpret the given isovalue. The default "Normal" method uses the isovalue without modification. The "Contained" and "Squared" method finds the isosurface that contains the given percentage of the integrated field, and integrated squared field, respectively. The "Volume" method finds the isosurface that matches the given percentage of the total grid volume.

The second line controls the color mapping. The Hue, Saturation   and Value fields give you the option to specify two colors. The   colormap option gives you an option to change how the transition   from one color to the other goes. The default colormap is the   Diverging colormap: it goes from one pure color to white to the   other pure color. Another colormap implemented is the Rainbow   colormap: it goes from one color to the other color via other   pure colors. 

The third line allows you to control a clipping plane, cutting   through the isosurface so you can look inside. 

.. rst-class:: steps

  \ 
    | Select the Rainbow Colormap

.. image:: /Images/VisualizationOfDensitiesEtc/t14-anthracene-rainbow-iso.png

In general the Divergent colormap makes it easier to see small   variations in some property, although the Rainbow colormap is   obviously much more colorful. If you have a symmetric scalar   range, the divergent colormap will put the zero value at the   white color. For the electrostatic potential this is not useful,   but for example for a difference density it makes sense: 

.. rst-class:: steps

  \ 
    | Delete the Colored Isosurface (use the left pull-down menu on that line)
    | **Fields → Calculated**
    | In the Calculated Field C-1 controls: select left field **Density → SCF**
    | In the Calculated Field C-1 controls: select right field **Density → Density Sum Frag**
    | **Add → Isosurface: Colored**
    | In the Colored Isosurface line: Left field selector at bottom: **Density → SCF**
    | In the Colored Isosurface line: Right field selector at bottom: **Other → C-1**
    | In the Colored Isosurface line: change isovalue to 0.1
    | In the Colored Isosurface line: show the color legend
    | In the Colored Isosurface line: Specify a symmetric scalar range like -0.025 to 0.025

.. image:: /Images/VisualizationOfDensitiesEtc/t14-anthracene-symmetric-range.png

Step 3: Multi Isosurface
========================

An even better way to see what happens to the density when   forming a molecule out of the atomic fragments can be made using   the multi-iso option. The idea is that a whole set of isosurfaces   is generated, for a range of iso values. The surfaces will be   colored by there isovalue. 

.. rst-class:: steps

  \ 
    | In the Colored Isosurface line: Use the Delete command from the left pull-down menu 
    | 
    | **Add → Isosurface: Multi**
    | 
    | In the Multi Isosurface line: 
    | in the field select menu select the density difference:  **Other → 1 → C-1**
    | set N (the number of isosurfaces) to 7
    | change the min-max range to -0.01 ... 0.01
    |
    | Click on the -XY button to use a Clip plane in the XY plane 
    | (the sign determines from which side you can see)
    |
    | Use cmd/ctrl - Minus repeatedly to make the atomic spheres very small
    | 
    | **Fields → Grid → Fine**
    | Click OK to confirm recalculating the fields
    | 
    | Rotate and zoom to get a good view

.. image:: /Images/VisualizationOfDensitiesEtc/t14-anthracene-difference-density.png

Now you can very clearly see that the electron density in the   bonds is increased (blue), and where that electron density comes   from (everywhere else, including close to the atoms) 

The clip plane allows you to cut away part of an isosurface, such   that you can look inside. The buttons on the last detail line   allow you to position the clip plane as needed. 

Instead of using a clipping plane you can make the isosurfaces   transparent: 

.. rst-class:: steps

  \ 
    | Remove the clipping plane (uncheck the Use Clip Plane check box)
    | Change the Opacity to 20 %
    | **View → View Direction → Along Z-axes**
    | Zoom a little closer

.. image:: /Images/VisualizationOfDensitiesEtc/t14-anthracene-transparent-isosurface.png

Step 4: Combining visualization techniques
==========================================

You can also combine several visualization methods in one image. 

.. rst-class:: steps

  \ 
    | In the Isosurface: Multi line
    | set Opacity to 100
    | click the -XY button to use a clipping plane
    | rotate to look from the side
    | Check the "Interactive Plane" check box
    | Drag the red line to move the clipping plane slightly above the atom plane 
    | (you might need to use the -XY button to realign it first)
    | UnCheck the "Interactive Plane" check box
    | 
    | **Add → Cut Plane: Colored**
    | In the Cut Plane: colored line
    | Select the C-1 field
    | Select three atoms, and click the Position plane with atoms button
    | (note you can select atoms by shift-dragging a rectangle around an atom, 
    | repeating this trick 3 times)
    | Use the same scalar range as for the Multi Isosurface (without log option!)
    | Zoom to get a close view

Now you get a picture using the multi-iso and colored plane   options at the same time. 

.. image:: /Images/VisualizationOfDensitiesEtc/t14-anthracene-multiiso-cutplane.png

Step 5: Play with lights
========================

AMSview has also some options to control lights. This allows you   to change an image the way you like it by adding a directed light   source that casts shadows. You can also control the amount of   ambient light and directed light. It is hard in general to say   what is the best setting, so just try and play around: 

.. rst-class:: steps

  \ 
    | **View → Show Scene Light**
    | 
    | In the extra scene light line (the topmost of the control lines at the bottom):
    | Check the box to turn the light on
    | Check the box to position the light
    | Position the light as you like it 
    | (you may have to rotate to be able to control the light properly)
    | Change the intensity of the extra light and the ambient light 
    | (the Scene/Camera light controls)
    | Uncheck the box to position the light
    | Rotate and zoom as you prefer

One possible image you can make this way looks like this: 

.. image:: /Images/VisualizationOfDensitiesEtc/t14-play-with-lights.png

Step 6: Special fields
======================

AMSview has access to a few fields that need extra clarification. One of these is the Steric Interaction, which uses the Van der Waals radius to visualize steric bulk. The field is the minimum distance to the Van der Waals surface of the selected atoms.

.. rst-class:: steps

  \
    | Delete the other surfaces present
    | Add an isosurface
    | Select an hydrogen atom
    | **Select → Select Atoms Of Same Type**
    | At the bottom click Select Field... and choose Properties → Steric Interaction 1.

It is possible to make different selections and generate their own Steric Interaction field.

.. image:: /Images/VisualizationOfDensitiesEtc/t14-stericinteraction.png
