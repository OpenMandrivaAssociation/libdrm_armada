%define major	0
%define	snap	20150420
%define libname	%mklibname drm_armada %{major}
%define devname	%mklibname -d drm_armada

Summary:	Kernel DRM service interface
Name:		libdrm-armada
Version:	0.0.0
Release:	0.%{snap}.1
License:	LGPLv2+
Group:		System/Libraries
Url:		ftp.arm.linux.org.uk/~rmk/libdrm-armada.git
# git clone git://ftp.arm.linux.org.uk/~rmk/libdrm-armada.git
Source0:	%{name}-%{version}-%{snap}.tar.xz
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(libdrm)

%description
Userspace interface to kernel DRM services -- development files
This library implements the userspace interface to the kernel DRM
services.  DRM stands for "Direct Rendering Manager", which is the
kernelspace portion of the "Direct Rendering Infrastructure" (DRI).
The DRI is currently used on Linux to provide hardware-accelerated
OpenGL drivers.

%package -n	%{libname}
Summary:	Library for accessing USB devices
Group:		System/Libraries

%description -n	%{libname}
Userspace interface to kernel DRM services -- development files
This library implements the userspace interface to the kernel DRM
services.  DRM stands for "Direct Rendering Manager", which is the
kernelspace portion of the "Direct Rendering Infrastructure" (DRI).
The DRI is currently used on Linux to provide hardware-accelerated
OpenGL drivers.

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package includes the development files for %{name}.

%prep
%setup -qn %{name}-%{version}-%{snap}
autoreconf -fiv

%build
%configure \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libdrm_armada.so.%{major}*

%files -n %{devname}
%{_libdir}/libdrm_armada.so
%{_includedir}/libdrm/
%{_libdir}/pkgconfig/libdrm_armada.pc
