#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-FNN
Version  : 1.1.3.1
Release  : 48
URL      : https://cran.r-project.org/src/contrib/FNN_1.1.3.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/FNN_1.1.3.1.tar.gz
Summary  : Fast Nearest Neighbor Search Algorithms and Applications
Group    : Development/Tools
License  : GPL-2.0+ LGPL-2.1
Requires: R-FNN-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
including KNN classification, regression and information measures are implemented.

%package lib
Summary: lib components for the R-FNN package.
Group: Libraries

%description lib
lib components for the R-FNN package.


%prep
%setup -q -c -n FNN
cd %{_builddir}/FNN

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653342181

%install
export SOURCE_DATE_EPOCH=1653342181
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library FNN
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library FNN
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library FNN
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc FNN || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/FNN/COPYRIGHTS
/usr/lib64/R/library/FNN/DESCRIPTION
/usr/lib64/R/library/FNN/INDEX
/usr/lib64/R/library/FNN/Meta/Rd.rds
/usr/lib64/R/library/FNN/Meta/features.rds
/usr/lib64/R/library/FNN/Meta/hsearch.rds
/usr/lib64/R/library/FNN/Meta/links.rds
/usr/lib64/R/library/FNN/Meta/nsInfo.rds
/usr/lib64/R/library/FNN/Meta/package.rds
/usr/lib64/R/library/FNN/NAMESPACE
/usr/lib64/R/library/FNN/R/FNN
/usr/lib64/R/library/FNN/R/FNN.rdb
/usr/lib64/R/library/FNN/R/FNN.rdx
/usr/lib64/R/library/FNN/help/AnIndex
/usr/lib64/R/library/FNN/help/FNN.rdb
/usr/lib64/R/library/FNN/help/FNN.rdx
/usr/lib64/R/library/FNN/help/aliases.rds
/usr/lib64/R/library/FNN/help/paths.rds
/usr/lib64/R/library/FNN/html/00Index.html
/usr/lib64/R/library/FNN/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/FNN/libs/FNN.so
/usr/lib64/R/library/FNN/libs/FNN.so.avx2
/usr/lib64/R/library/FNN/libs/FNN.so.avx512
