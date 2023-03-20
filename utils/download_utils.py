import pathlib
import urllib.request
from zipfile import ZipFile


def download_figshare(
    figshare_id, output_file, figshare_url="https://ndownloader.figshare.com/files/"
):
    """
    Download the provided figshare resource

    Attributes
    ----------
    figshare_id : str
        string of numbers that corresponds to the figshare identifier
    output_file : pathlib.Path
        the location and file name of where to save the downloaded data
    figshare_url: str, default "https://ndownloader.figshare.com/files/"
        the location of where the figshare id is stored
    """
    urllib.request.urlretrieve(f"{figshare_url}/{figshare_id}", output_file)


def download_depmap_bucket(
    file_name,
    output_dir,
    bucket="depmap-external-downloads",
    resource="pharmacological_profiling",
):
    """
    Download a legacy depmap file not stored on figshare

    Attributes
    ----------
    file_name : str
        name of the file to download, this will also be the name of the downloaded file
    output_dir : pathlib.Path
        the directory of where to save the file (directory only)
    bucket: str, default "depmap-external-downloads"
        the name of the bucket where the DepMap data are stored
    resource: str, default "pharmacological_profiling"
        the category of DepMap resource
    """

    # Build the url to retrieve
    base_url = "https://depmap.org/portal/download/api/download"
    file_url = f"?file_name=ccle_legacy_data%2F{resource}%2F{file_name}&bucket={bucket}"

    download_url = f"{base_url}{file_url}"

    urllib.request.urlretrieve(download_url, pathlib.Path(output_dir, file_name))


def download_nci60(
    output_file,
    base_url,
    attachment_id,
    attachment_name,
    version="6",
    modification_date=1672801037000,
    api="v2",
    extract_zip=False,
):
    """
    Download the given nci-60 resource

    Attributes
    ----------
    output_file : pathlib.Path()
        the location to save the downloaded file
    base_url : str
        url to download from
    attachment_id : str
        the unique file identifier
    attachment_name: str
        the name of the file attachment
    version: str, default = "6"
        the nci60 data version
    modification_date: str, default "1672801037000"
        the identifier indicating last modification time for version control
    api: str, default = "v2"
        the version of the API used to download the file
    extract_zip, bool, default = False
        whether or not to extract the zip file
    """
    request_string = f"{base_url}/{attachment_id}/{attachment_name}?version={version}&modificationDate={modification_date}&api={api}"

    urllib.request.urlretrieve(request_string, output_file)

    if extract_zip:
        with ZipFile(output_file) as z:
            z.extractall(path=output_file.parent)
