%define oversion V39

Summary:       Squeak Sources
Name:          squeak-sources
Version:       3.9
Release:       %mkrel 1
License:       Free with restrictions (http://www.squeak.org/download/license.html)
Group:         Development/Other
Source0:       ftp://st.cs.uiuc.edu/Smalltalk/Squeak/3.0/platform-independent/Squeak%oversion.sources.gz
URL:           http://www.squeak.org
BuildRequires: gzip
Requires:      squeak-vm >= 3.0
Requires:      squeak-image >= 3.0.3552
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
These are the source files needed for the Squeak Virtual Machiene.

%build
mkdir -p %{buildroot}/extract/
cp %{SOURCE0} %{buildroot}/extract/; gunzip -f %{buildroot}/extract/Squeak%oversion.sources.gz

%install
mkdir -p %{buildroot}%{_libdir}/squeak/
mv %{buildroot}/extract/Squeak%oversion.sources %{buildroot}%{_libdir}/squeak/
rm -rf %{buildroot}/extract/

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%{_libdir}/squeak/*
