
%define	pname	XMMS

Summary:	A fancy desklet that allows you to control XMMS from the desktop
Summary(pl):	Ozdobny desklet pozwalaj±cy sterowaæ XMMS-em z pulpitu
Name:		gDesklets-%{pname}
Version:	2
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://gdesklets.gnomedesktop.org/files/xmms-%{version}.tgz
# Source0-md5:	64b17f0098fa30d45fc8fe0a6d519d43
URL:		http://gdesklets.gnomedesktop.org/categories.php?func=gd_show_app&gd_app_id=42
BuildRequires:	python >= 2.3
BuildRequires:	python-pygtk-gtk >= 1.99.14
Requires:	gDesklets
Requires:	python-xmms
Provides:	gDesklets-display
Provides:	gDesklets-sensor
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_sensorsdir	%{_datadir}/gdesklets/Sensors
%define _displaysdir	%{_datadir}/gdesklets/Displays

%description
A fancy desklet that allows you to control XMMS from the desktop.

%description -l pl
Ozdobny desklet pozwalaj±cy sterowaæ XMMS-em z pulpitu.

%prep
%setup -q -n %{pname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sensorsdir},%{_displaysdir}/%{pname}}

./Install_%{pname}_Sensor.bin --nomsg \
	$RPM_BUILD_ROOT%{_sensorsdir}

cp -R Display/gfx Display/*.display $RPM_BUILD_ROOT%{_displaysdir}/%{pname}

find $RPM_BUILD_ROOT%{_sensorsdir}/%{pname} -name "CVS" |xargs rm -rf

%py_comp $RPM_BUILD_ROOT%{_sensorsdir}
%py_ocomp $RPM_BUILD_ROOT%{_sensorsdir}

rm -f $RPM_BUILD_ROOT%{_sensorsdir}/*/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%{_sensorsdir}/%{pname}/*.py[co]
%{_displaysdir}/*
