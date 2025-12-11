{pkgs}: {
  channel = "stable-24.05";
  packages = [
    pkgs.python312
    pkgs.python312Packages.pip
  ];
  idx.extensions = [
    "ms-python.python"
  ];
  idx.workspace.onCreate = {
    install-deps = "pip install -r requirements.txt";
  };
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
