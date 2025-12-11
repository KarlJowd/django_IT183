{pkgs}: {
  channel = "stable-24.05";
  packages = [
    pkgs.python312
  ];
  idx.extensions = [
    "ms-python.python"
  ];
  idx.previews = {
    previews = {
      web = {
        command = [
          "python"
          "manage.py"
          "runserver"
          "0.0.0.0:$PORT"
          "--noreload"
          "--insecure"
        ];
        manager = "web";
      };
    };
  };
}
