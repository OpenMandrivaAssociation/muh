%define name	muh
%define version	2.1
%define release	%mkrel 0.rc1.6
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


%preun
%_remove_install_info %{name}.info

%files
%defattr(-,root,root)
%doc AUTHORS INSTALL VERSION
%{_bindir}/%{name}*
%{_infodir}/%{name}*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1:2.1-0.rc1.6mdv2011.0
+ Revision: 620418
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1:2.1-0.rc1.5mdv2010.0
+ Revision: 430118
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 1:2.1-0.rc1.4mdv2009.0
+ Revision: 140966
- restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1:2.1-0.rc1.4mdv2008.1
+ Revision: 130348
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import muh


* Wed Dec 22 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.1-0.rc1.4mdk
- fix summary

* Thu Aug 19 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.1-0.rc1.3mdk
- rebuild

* Wed Jul 02 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.1-0.rc1.2mdk
- disable ipv6, although it should'nt disable ipv4, I cannot get it working myself..

* Tue Feb 04 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.1-0.rc1.1mdk
- Add Epoch tag to fix versioning mess
- 2.1rc1
- Build with ipv6 support(I was wrong, it won't disable ipv4 support)
- bzip2 sources
- Include an updated muhrc for making it (slightly) easier to use ipv6
- man pages obsoleted by info
- Remove license from doc's as it's GPL

* Wed Oct 15 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.06a-4mdk
- from Per Øyvind Karlsen <peroyvind@delonic.no> :
	- Fix wrapper

* Wed Oct 09 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.06a-3mdk
- from Per Øyvind Karlsen <peroyvind@delonic.no> :
	- Fix description
	- Fix doc permissions
	- Do not build ipv6-support unless defined (it will disable ipv4)
	- Added a wrapper for configdir check

* Wed Oct  9 2002 Per Øyvind Karlsen <peroyvind@delonic.no> 2.06a-2mdk
- Clean
- Define ipv6 for support or not
- %%build(stupidstupidstupidstupid)
- Typo

* Wed Oct  9 2002 Per Øyvind Karlsen <peroyvind@delonic.no> 2.06a-1mdk
- Initial release
