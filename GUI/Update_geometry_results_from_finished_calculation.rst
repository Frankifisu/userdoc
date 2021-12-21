Update geometry dialog
***********************

When opening AMSinput for a finished job, or if the AMSinput window is open when the job finishes, the following dialog pops up:

.. image:: /images/update_dialog.png
   :width: 80%
   :align: center

If you click

* **No**: The original input is preserved.
* **Yes, new job**: This creates a new job, so that you do not overwrite the original job. The geometry is updated from the results file, and new input options are set based on the checkbox selection (see below).
* **Yes**: This reuses the same input file. The geometry is updated from the results file. **You should not check any of the checkboxes**, since a job cannot be restarted from itself.

Meaning of restart options
===========================

* **Use Hessian from results for AMS restart**: If you calculated the **hessian, normal modes, or vibrational frequencies** in the original job, you can reuse the calculated hessian in a new job. This can help, for example, to converge a geometry optimization or transition state search faster. If you select the option, then on the **Details → Geometry Optimization** panel the **Initial Hessian** keyword is set to **From File**, and the **Initial Hessian from** is set to the engine.rkf file from the original job.

* **Use MD velocities from results for AMS MD restart**: If the original job is a molecular dynamics simulation, this option will load the velocities from the final frame from the original job, allowing you to continue an MD simulation. Note that if you use thermostats or barostats, the continuation trajectory will not perfectly match the trajectory which "would have" taken place if the original job was longer. If you select the option, then on the **Model → MD** panel, the **Initial velocities** keyword is set to **From File**, and the **File** is set to the ams.rkf file from the original job.

* **Restart engine with engine results**: If the original job is an ADF/BAND/DFTB job, this option lets you continue from the converged SCF solution in the original job. The other engines do not use engine restart information. If you select the option, then on the **Model → Restart** panel, the **Engine restart** keyword is set to the engine.rkf file from the original job.

