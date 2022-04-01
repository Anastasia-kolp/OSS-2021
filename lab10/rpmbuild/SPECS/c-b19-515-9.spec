Name:       c-b19-515-9
Version:    1.0
Release:    1%{?dist}
Summary:    Программа студента Колпаковой Анастасии группы Б19-515
Group:      Testing
License:    GPL
URL:        https://github.com/Anastasia-kolp/OSS-2021
Source0:     %{name}-%{version}.tar.gz
BuildRequires: gcc

%description
A test package

%prep
%setup -q

%build
gcc -g -O2 -o c-b19-515-9 c-b19-515-9.c

%install
mkdir -p %{buildroot}%{_bindir}
cp c-b19-515-9 %{buildroot}%{_bindir}
sudo rpm -i ~/rpmbuild/RPMS/noarch/b19-515-9-1.0-1.el8.noarch.rpm --force

%files
%{_bindir}/c-b19-515-9

%changelog
* Thu Oct 16 2012 Колпакова
- Added %{_bindir}/c-b19-515-9
