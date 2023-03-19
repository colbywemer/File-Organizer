import os
import shutil
# Define the source and destination directories
src = os.path.join(os.path.expanduser("~"), "Downloads")
dirs = {
    "img": os.path.join(src, "Images"),
    "exe": os.path.join(src, "Programs"),
    "doc": os.path.join(src, "Documents"),
    "zip": os.path.join(src, "Compressed"),
    "ppt": os.path.join(src, "Powerpoint"),
    "mp3": os.path.join(src, "Audio"),
    "mp4": os.path.join(src, "Video"),
    "excel": os.path.join(src, "Data"),
    "html": os.path.join(src, "Webpage"),
    "code": os.path.join(src, "Code"),
    "misc": os.path.join(src, "Misc"),
}
extension_dict = {
    (".java", ".cpp", ".h", ".class", ".py", ".c", ".cs", ".m", ".swift", ".vb", ".rb", ".pl", ".scala",
        ".go", ".kt", ".rs", ".lua", ".ps1", ".psm1", ".psc1", ".psc2", ".d", ".hs", ".lhs", ".mli", ".ml",
        ".mll", ".mly", ".r", ".jl", ".dart", ".fs", ".fsi", ".fsx", ".fsharp", ".s", ".asm", ".sql",
        ".vue", ".bas", ".clj", ".cljs", ".cljc", ".groovy", ".erl", ".hrl", ".ex", ".exs", ".mlp",
        ".cmake", ".yml", ".yaml", ".ini", ".cfg", ".conf", ".tf", ".tfvars", ".tfstate",
        ".tfstate.backup", ".nim", ".nimble", ".nimrod", ".v", ".vh", ".sv", ".svh", ".vhd", ".xdc",
        ".tcl", ".perl", ".pm", ".t", ".awk", ".p", ".pas", ".las", ".lp", ".lsp", ".scm", ".st", ".prg",
        ".lst", ".mod", ".jcl", ".mac", ".f", ".f90", ".f95", ".sas", ".b", ".dpr", ".dproj", ".groupproj",
        ".bdsgroup", ".bdsgroupitem", ".dfm", ".nfm", ".ndk", ".pk", ".bpk", ".res", ".tlb", ".tlh", ".dcr",
        ".dpk", ".drc", ".cbl", ".cob", ".cpy", ".asm", ".mac", ".map", ".mm", ".pbxproj", ".pbxuser",
        ".xcworkspace", ".xcworkspacedata", ".xcscheme", ".xcuserstate", ".xib", ".storyboard", ".plist",
        ".rc", ".def", ".defn", ".hpp", ".cppm", ".icn", ".scrbl", ".ss", ".sc", ".cljs.hl", ".rkt", ".scm",
        ".rst", ".pxd", ".pyx", ".pxi", ".fut", ".futhark", ".sml", ".mlton"): dirs["code"],
    (".html", ".htm", ".xhtml", ".shtml", ".css", ".js", ".jsx", ".php", ".ttf", ".woff", ".otf",
    ".asp", ".jsp", ".php8", ".php7", ".php5", ".ts", ".tsx", ".json", ".md", ".markdown", ".mdwn",
    ".mdown", ".mkd", ".mkdn", ".xsl", ".dtd", ".ent", ".ipynb", ".rss", ".atom", ".svg", ".webp"): dirs["html"],
    (".exe", ".jar", ".msi", ".app", ".dmg", ".sh",
    ".bat", ".deb", ".rpm", ".ps", ".pssc", ".pkg"): dirs["exe"],
    (".csv", ".xlsx", ".xls", ".ods", ".tsv", ".accdb", ".mdb", ".dbf"): dirs["excel"],
    (".mp4", ".avi", ".wmv", ".mov", ".flv", ".webm", ".mkv", ".m4v", ".3gp", ".3g2", ".mpg", ".mpeg",
    ".m2v", ".mpe", ".vob", ".ogv", ".gifv", ".asf", ".rm", ".rmvb"): dirs["mp4"],
    (".mp3", ".wav", ".aiff", ".aac", ".ogg", ".wma", ".flac", ".alac", ".m4a", ".m4b", ".opus", ".ra",
    ".mid", ".midi", ".amr", ".pcm", ".wm"): dirs["mp3"],
    (".ppt", ".pptx", ".odp"): dirs["ppt"],
    (".zip", ".rar", ".tar", ".gz", ".bz2", ".7z", ".xz", ".tar.gz", ".tgz", ".tar.bz2", ".tbz2",
    ".tar.xz", ".txz", ".vcf", ".ics", ".tar.z"): dirs["zip"],
    (".doc", ".docx", ".txt", ".rtf", ".odt", ".pdf"): dirs["doc"],
    (".jpg", ".png", ".jpeg", ".ico", ".gif", ".bmp", ".tif", ".tiff", ".raw", ".svgz", ".eps", ".ai",
    ".psd"): dirs["img"],
}


def check_extension(src_path, extensions):
    return any(os.path.splitext(file)[1] in extensions for _, _, files in os.walk(src_path) for file in files)


def check_file_extension(ext):
    for key in extension_dict.keys():
        if ext.endswith(key):
            return extension_dict[key]
    return "misc"


paths = dirs.values()
for path in paths:
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            folder = os.path.basename(path)
            print(f"Created Folder \"{folder}\"")
    except:
        print(f"There was an error creating folder \"{folder}\"")


folders = {f.name for f in os.scandir(src) if f.is_dir() and f.path not in paths}


for folder in folders:
    try:
        src_path = os.path.join(src, folder)
        dest_path = ""
        for key, value in extension_dict.items():
            if check_extension(src_path, key):
                dest_path = os.path.join(value, folder)
                shutil.move(src_path, dest_path)
                print(f"Moved \"{folder}\" Folder To \"{os.path.basename(value)}\" Folder")
                break
        else:
            misc_path = os.path.join(dirs["misc"], folder)
            shutil.move(src_path, misc_path)
            print(f"Moved \"{folder}\" Folder To Misc Folder")
    except:
        print(f"There was an error moving \"{folder}\" Folder")


for entry in os.scandir(src):
    if entry.is_file():
        ext = os.path.splitext(entry.name)[1].lower()
        dst = check_file_extension(ext)
        try:
            entry_path = os.path.join(src, entry)
            shutil.move(entry_path, os.path.join(dst, entry.name))
            print(f"Moved \"{entry.name}\" To \"{os.path.basename(dst)}\" Folder")
        except:
            print(f"There Was An Error Moving \"{entry.name}\"")