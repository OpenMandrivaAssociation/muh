%define name	muh
%define version	2.1
%define release	%mkrel 0.rc1.5
#(peroyvind) ipv6 support seems to break ipv4 support
%define ipv6    0
%if %ipv6
%define	Summary	A full featured irc bouncer with IPV6-support
%else
%define	Summary	A full featured irc bouncer
%endif

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL 
Group:		Networking/IRC
Source0:	%{name}-%{version}rc1.tar.bz2
Source1:	%{name}.sh.bz2
Source2:	%{name}rc.bz2
URL: 		http://mind.riot.org/muh/
Summary:	%{Summary}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Epoch:		1

%description
muh is a quite versatile irc-bouncer for unix. An irc-bouncer is a program
that acts as a middleman between your irc-client and your irc-server.
If you have no idea what this is good for you probably don't need it.

Some of muh's features: 
* a permanent connection to the irc-server is maintained - 
 on networks without noteservs/nickservs this can be handy
 (guard your nick, log messages from your friends) 
* dcc-bouncing (+resume) 
* customizable logging 
* flood-protection (optionally ignore people host-based) 
* message-logging (+forwarding to e.g. an email-address) 
* vhost-support 
%if %ipv6
* ipv6-support
%endif

%prep
%setup -q -n %{name}-%{version}rc1

%build
%configure \
	--datadir=%{_datadir}/%{name} \
%if %ipv6
	--enable-ipv6
%endif

%make

%install 
rm -rf ${RPM_BUILD_ROOT}
#fix permissions on docs
chmod 644 AUTHORS INSTALL COPYING VERSION
%{makeinstall_std}
mv $RPM_BUILD_ROOT%{_bindir}/{%{name},%{name}.bin}
bzcat %{SOURCE1} > $RPM_BUILD_ROOT%{_bindir}/%{name}; chmod 755 $RPM_BUILD_ROOT%{_bindir}/%{name}
bzcat %{SOURCE2} > $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}rc; chmod 644 $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}rc

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%files
%defattr(-,root,root)
%doc AUTHORS INSTALL VERSION
%{_bindir}/%{name}*
%{_infodir}/%{name}*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

