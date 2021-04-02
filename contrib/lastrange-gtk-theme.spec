%global tname       LaStrange
%global git_date    20210402
# https://github.com/zibonbadi/lastrange-gtk-theme/commit/3d995f977f88693cce76ed8f54c3b4f47aa0fee7
%global git_commit  3d995f977f88693cce76ed8f54c3b4f47aa0fee7
%global git_commit_short  %(c="%{git_commit}"; echo ${c:0:8})

Name:           lastrange-gtk-theme
Version:        %{git_date}
Release:        0.1.git%{git_commit_short}%{?dist}
Summary:        A clean, simple XFWM/GTK3 theme for easy and focused computing
License:        GPLv3+
URL:            https://github.com/zibonbadi/lastrange-gtk-theme
Source0:        https://github.com/zibonbadi/lastrange-gtk-theme/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils

Requires:       gtk3 >= 3.22.20
Requires:       lastrange-icon-theme
Requires:       gtk-murrine-engine

%description
A clean, simple icon theme for easy and focused computing. Originally
developed for dogfooding, the theme aims to be simple in both design
and implementation while keeping a distinctly Unix-like aesthetic
...with some modern quality-of-life considerations.

The name is a reference to Tom LaStrange, the inventor of the TWM
window manager, which served as the main inspiration for the desktop
theme. Other influences include printed paper, the Athena widget
library and the Amiga Workbench

%prep
%autosetup -p1 -n %{name}-%{git_commit}
find . -executable -type f -exec chmod --verbose a-x '{}' ';'
# Use the matching icon theme.
sed -i -e 's,IconTheme=Vertex-Maia,IconTheme=LaStrange,g' \
    LaStrange*/index.theme

%install
mkdir -p %{buildroot}%{_datadir}/themes/%{tname}
cp -a %{tname} %{tname}-industrial %{tname}-solarized \
    %{buildroot}%{_datadir}/themes/

%files
%license README.md
%doc README.md banner.png
%{_datadir}/themes/%{tname}
%{_datadir}/themes/%{tname}-industrial
%{_datadir}/themes/%{tname}-solarized

%changelog
* Fri Apr 02 2021 Joel Barrios <http://www.alcancelibre.org/> - 20210402-0.1.git3d995f97
- Initial spec file.
