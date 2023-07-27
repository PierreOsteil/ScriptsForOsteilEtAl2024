//This macro will seperate the channels of a merged image and convert the z-slices into time frames to be compatable with StarDist plugin. 
//The nuclei of the DAPI images will be segmented in Stardist plugin to create ROIs.
//ROIs will be measured before being deleted to be ready for the next image.

//Ask the user to select the source directory
dir1 = getDirectory("Select the source directory");

//Ask the user to select the destination directory
dir2 = getDirectory("Choose the destination directory");

//Generate a list of the files in the selected directory
list = getFileList(dir1);
Array.sort(list);

	for(i=0;i<list.length;i++){	
	fileName = dir1 + list[i];
	if(endsWith(fileName,"czi")){
		//use the Bio-FOrmats importer to open the file
		run("Bio-Formats Importer", "open=["+fileName+"] autoscale color_mode=Colorized rois_import=[ROI manager] view=Hyperstack stack_order=XYCZT");
	
		//Store the initial image name into the nameStore variable
		nameStore = getTitle();
	
		//Split the channels into red and blue
		run("Split Channels");

		numSlices=nSlices;

		//Rename the channels according to their stain and separate the z slices
		selectWindow("C3-"+nameStore);
		rename("DAPI");
		run("Properties...", "channels=1 slices=1 frames="+numSlices+" pixel_width=1 pixel_height=1 voxel_depth=1");
		
		selectWindow("C4-"+nameStore);
		rename("561");
		run("Properties...", "channels=1 slices=1 frames="+numSlices+" pixel_width=1 pixel_height=1 voxel_depth=1");
	
		selectWindow("C1-"+nameStore);
		rename("488");
		run("Properties...", "channels=1 slices=1 frames="+numSlices+" pixel_width=1 pixel_height=1 voxel_depth=1");

		selectWindow("C2-"+nameStore);
		rename("633");
		run("Properties...", "channels=1 slices=1 frames="+numSlices+" pixel_width=1 pixel_height=1 voxel_depth=1");
		
		//segment the nuclei using Stardist plugin, creating labels and measure the intensity of DAPI, 488 and 594 channels
		
		run("Command From Macro", "command=[de.csbdresden.stardist.StarDist2D], args=['input':'DAPI', 'modelChoice':'Versatile (fluorescent nuclei)', 'normalizeInput':'true', 'percentileBottom':'1.0', 'percentileTop':'99.8', 'probThresh':'0.7', 'nmsThresh':'0.4', 'outputType':'Both', 'nTiles':'1', 'excludeBoundary':'2', 'roiPosition':'Automatic', 'verbose':'false', 'showCsbdeepProgress':'false', 'showProbAndDist':'false'], process=[false]");
			
		selectWindow("DAPI");
		roiManager("Measure");
			
		selectWindow("488");
		roiManager("Measure");
		
		selectWindow("561");
		roiManager("Measure");

		selectWindow("633");
		roiManager("Measure");
			
		//Save the ROIs, then delete. Save the labeled image and close.
		roiManager("Save", dir2+nameStore+"RoiSet.zip");
		roiManager("Delete");
		selectWindow("Label Image");
		rename(nameStore+"-Label Image");
		saveAs("Tiff", dir2+nameStore+"-Label Image.tif");
		close(nameStore+"-Label Image");

		run("Close All");
		
	}}

	//Save the raw data and close. Close all images.
	saveAs("Results", dir2+"Results.csv");
	close("Results");
	