%global srcname fast_tls


Name: erlang-%{srcname}
Version: 1.0.7
Release: %mkrel 2

Group:   Development/Erlang

License: ASL 2.0
Summary: TLS / SSL native driver for Erlang / Elixir
URL: https://github.com/processone/%{srcname}/
Source0: https://github.com/processone/%{srcname}/archive/%{version}.tar.gz
# Set the default cipher list to PROFILE=SYSTEM.
# https://fedoraproject.org/wiki/Packaging:CryptoPolicies
Patch0: 0000-Use-the-system-ciphers-by-default.patch

Provides:  erlang-p1_tls = %{version}-%{release}
Obsoletes: erlang-p1_tls < 1.0.1

BuildRequires: erlang-rebar
BuildRequires: openssl-devel

Requires: erlang-p1_utils >= 1.0.5

%{?__erlang_drv_version:Requires: %{__erlang_drv_version}}
%{?__erlang_nif_version:Requires: %{__erlang_nif_version}}


%description
TLS / SSL native driver for Erlang / Elixir. This is used by ejabberd.


%prep
%setup -n %{srcname}-%{version} -q

%patch0


%build
%{rebar_compile}


%install
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib

install -pm755 priv/lib/* $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/
%{erlang_install}


%files
%license LICENSE.txt
%doc README.md
%{erlang_appdir}



%changelog
* Tue Nov 22 2016 neoclust <neoclust> 1.0.7-2.mga6
+ Revision: 1068728
- Rebuild against core openssl

* Thu Nov 17 2016 neoclust <neoclust> 1.0.7-1.mga6
+ Revision: 1067992
- imported package erlang-fast_tls

