{pkgs}: {
  channel = "stable-24.05";
  packages = [
    pkgs.python312
  ];
  idx.extensions = [
    "ms-python.python"
  ];
  idx.workspace.onCreate = {
    create-venv = "python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt";
  };
  idx.workspace.onStart = {
    activate-venv = "source .venv/bin/activate";
  };
  idx.previews = {
    previews = {
      web = {
        command = [
          "sh"
          "-c"
          "source .venv/bin/activate && python manage.py runserver 0.0.0.0:$PORT --noreload --insecure"
        ];
        manager = "web";
      };
    };
  };
}
