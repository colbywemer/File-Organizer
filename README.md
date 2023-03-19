# File Organizer
This Python script helps you organize your files by moving them to directories based on their file extensions.
## Requirements
File Organizer requires the following Python libraries:  
'os'  
'shutil'  
You can install these libraries by running the command pip install -r requirements.txt. 
## Usage
1. Specify the source directory to organize the files from. By default, the program uses the Downloads directory in the user's home folder.
2. Run the program.
3. The program will categorize files into their respective folders based on their file extensions. Files with unknown file extensions will be moved to a "misc" folder.
## How To Use
1. Download the script and save it in a convenient location on your computer.
2. Open a terminal or command prompt and navigate to the directory where you saved the script.
3. Run the script by typing the following command and pressing Enter: python file_organizer.py
4. The script will move all files with the corresponding extensions to their designated directories.
## Supported File Extensions
***Images*** - .jpg, .png, .jpeg, .ico, .gif, .bmp, .tif, .tiff, .raw, .svgz, .eps, .ai, .psd  
***Programs*** - .exe, .jar, .msi, .app, .dmg, .sh, .bat, .deb, .rpm, .ps, .pssc, .pkg  
***Documents*** - .doc, .docx, .txt, .rtf, .odt, .pdf  
***Compressed*** - .zip, .rar, .tar, .gz, .bz2, .7z, .xz, .tar.gz, .tgz, .tar.bz2, .tbz2, .tar.xz, .txz, .vcf, .ics, .tar.z  
***Powerpoint*** - .ppt, .pptx, .odp  
***Audio*** - .mp3, .wav, .aiff, .aac, .ogg, .wma, .flac, .alac, .m4a, .m4b, .opus, .ra, .mid, .midi, .amr, .pcm, .wm  
***Video*** - .mp4, .avi, .wmv, .mov, .flv, .webm, .mkv, .m4v, .3gp, .3g2, .mpg, .mpeg, .m2v, .mpe, .vob, .ogv, .gifv, .asf, .rm, .rmvb  
***Data*** - .csv, .xlsx, .xls, .ods, .tsv, .accdb, .mdb, .dbf  
***Webpage*** - .html, .htm, .xhtml, shtml, .css, .js, .jsx, .php, .ttf, .woff, .otf, .asp, .jsp, .php8, .php7, .php5, .ts, .tsx, .json, .md, .markdown, .mdwn, .mdown, .mkd, .mkdn, .xsl, .dtd, .ent, .ipynb, .rss, .atom, .svg, .webp  
***Code*** - .java, .cpp, .h, .class, .py, .c, .cs, .m, .swift, .vb, .rb, .pl, .scala, .go, .kt, .rs, .lua, .ps1, .psm1, .psc1, .psc2, .d, .hs, .lhs, .mli, .ml, .mll, .mly, .r, .jl, .dart, .fs, .fsi, .fsx, .fsharp, .s, .asm, .sql, .vue, .bas, .clj, .cljs, .cljc, .groovy, .erl, .hrl, .ex, .exs, .mlp, .cmake, .yml, .yaml, .ini, .cfg, .conf, .tf, .tfvars, .tfstate, .tfstate.backup, .nim, .nimble, .nimrod, .v, .vh, .sv, .svh, .vhd, .xdc, .tcl, .perl, .pm, .t, .awk, .p, .pas, .las, .lp, .lsp, .scm, .st, .prg, .lst, .mod, .jcl, .mac, .f, .f90, .f95, .sas, .b, .dpr, .dproj, .groupproj, .bdsgroup, .bdsgroupitem, .dfm, .nfm, .ndk, .pk, .bpk, .res, .tlb, .tlh, .dcr, .dpk, .drc, .cbl, .cob, .cpy, .asm, .mac, .map, .mm, .pbxproj, .pbxuser, .xcworkspace, .xcworkspacedata, .xcscheme, .xcuserstate, .xib, .storyboard, .plist, .rc, .def, .defn, .hpp, .cppm, .icn, .scrbl, .ss, .sc, .cljs.hl, .rkt, .scm, .rst, .pxd, .pyx, .pxi, .fut, .futhark, .sml, .mlton
## Requesting Changes
If you would like to request changes to the way a file extension is handled, such as removing or moving it, or if you would like to see support for a file extension that is not currently included, please submit a request by opening an issue in the project's GitHub repository. We will review all requests and consider making changes to the file extension handling or adding support for the requested file extensions in future updates.
