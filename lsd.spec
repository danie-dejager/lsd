Name:           lsd
Version:        1.1.5
Release:        3%{?dist}
Summary:        The next gen ls command

License:        MIT
URL:            https://github.com/lsd-rs/lsd
Source0:        https://github.com/lsd-rs/lsd/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  upx

%description
This project is a rewrite of GNU ls with lots of added features like colors, icons, tree-view, more formatting options etc. The project is heavily inspired by the super colorls project.

%global debug_package %{nil}

%prep
%setup -q

%build
# Install Rust using curl
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
export PATH="$PATH:$HOME/.cargo/bin"
cargo build --release

%install
%global _build_id_links none
mkdir -p %{buildroot}/%{_bindir}
strip "target/release/lsd"
upx target/release/lsd
install -m 755 target/release/%{name} %{buildroot}/%{_bindir}/%{name}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
