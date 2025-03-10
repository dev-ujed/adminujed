//import BaseForm from "./public/components/forms/base/BaseForm.vue";
import vue from "vue";
//Components
import Inicio from "./public/components/Inicio.vue"; 

(function() {
	/* Base components
	---------------------------------------------------------------------- */
//Vue.component('base-form', BaseForm);
	// Vue.component('field-error', FieldError);
	// Vue.component('form-button', FormButton);
	// Vue.component('select-field', SelectField);
	// Vue.component('tabs-component', Tabs);
	// Vue.component('text-area', TextArea);
	// Vue.component('text-field', TextField);
	// Vue.component('file-field', FileField);
	// Vue.component('search-form', SearchForm);
	// Vue.component('numeric-text-field', NumericTextField);

	/* App components
	------------------------------------------------------------------------- */
	vue.component("inicio", Inicio);



	/**
	 * Vue instance
	 */
	const app = new vue({
		el: '#dashboard',

		components: { DashboardStudentMenu, UserBar },

		data: {
			path: document.body.getAttribute('data-root'),
			iconsMap: {},
			isLoading: true,
			isResizing: false,
			menu: null,
			menuFocusTrap: null,
			menuIsVisible: false,
			menuIsCollapsed: false,
			menuIsOpen: false,
			queryMenuMd: false,
			queryMenuLg: false,
			screenSize: '',
			selectedGroups: [],
			hasSchedule : false
		},

		computed: {
			lowestHour: function() {
				let minHours = [];

				for (const index in this.selectedGroups) {
					if (this.selectedGroups[index].length > 0) {
						const minHour = this.selectedGroups[index].reduce(
							(min, item) => {
								let hourItem = Number(item.hora_inicio.split(':')[0]);
								return (hourItem < min ? hourItem : min);
							},
							Number(this.selectedGroups[index][0].hora_inicio.split(':')[0])
						);

						minHours.push(minHour);
					}
				}

				if (minHours.length == 0) {
					return 8;
				}

			   return minHours.reduce((a,b) => a < b ? a : b);
			},

			highestHour: function() {
				let maxHours = [];

				for (const index in this.selectedGroups) {
					if (this.selectedGroups[index].length > 0) {
						const maxHour = this.selectedGroups[index].reduce(
							(max, item) => {
								let hourItem = Number(item.hora_fin.split(':')[0]);
								return (hourItem > max ? hourItem : max);
							},
							Number(this.selectedGroups[index][0].hora_fin.split(':')[0])
						);

					   maxHours.push(maxHour);
					}
				}

				if (maxHours.length == 0) {
					return 14;
				}

				return maxHours.reduce((a,b) => a > b ? a : b);
			},

			getHours: function() {
				let hours=[];
				const STANDARD_MIN_HOUR = 8;
				const STANDARD_MAX_HOUR = 14;
				let minimumHour = this.lowestHour<STANDARD_MIN_HOUR ? this.lowestHour:STANDARD_MIN_HOUR;
				let maximumHour = this.highestHour<STANDARD_MAX_HOUR ? STANDARD_MAX_HOUR : this.highestHour;

				for (let index = minimumHour; index <= maximumHour; index++) {
					hours.push(index+":"+"00");
				}

				return hours;
			}
		},

		mounted() {
			this.registerMenuBreakpoints();

			this.menu = document.querySelector('#db-menu');

			Vue.nextTick(() => this.isLoading = false);
		},

		methods: {
			/**
			 * Show or hide dashboard menu.
			 */
			toggleMenu() {
				const isOpening = this.screenSize === 'sm' ? ! this.menuIsVisible : this.menuIsCollapsed;

				if (isOpening && this.screenSize !== 'lg') {
					this.$emit('showMenuOverlay');
					Vue.nextTick(() => this.setMenuFocusTrap());
				}

				if (this.screenSize === 'sm') {
					this.menuIsOpen = ! this.menuIsOpen;
					this.menuIsVisible = ! this.menuIsVisible;
					this.menuIsCollapsed = false;
				}
				else {
					this.menuIsOpen = this.menuIsCollapsed;
					this.menuIsVisible = true;
					this.menuIsCollapsed = ! this.menuIsCollapsed;
				}

				// Handle preferences in Session Storage
				if (this.screenSize === 'lg') {
					sessionStorage.setItem('menuCollapsed', ! isOpening);
				}

				Vue.nextTick(() => {
					this.handleMenuFocus(isOpening);

					if (! isOpening) {
						this.destroyMenuFocusTrap();
					}
				});
			},

			/**
			 * Focus the appropiate element after opening or closing the main menu.
			 *
			 * @param {Boolean} isOpening
			 */
			handleMenuFocus(isOpening) {
				if (isOpening && this.screenSize === 'lg') {
					return this.menu.querySelector('button, [href], input, [tabindex="0"]').focus();
				}

				document.querySelector(isOpening ? '#main-menu-btn': '#user-bar-btn').focus();
			},

			/**
			 * Define the value for the `menuIsOpen` attribute
			 * after a resizing event.
			 */
			setMenuIsOpenAttribute() {
				this.menuIsOpen = ! (this.queryMenuMd.matches && ! this.queryMenuLg.matches);
			},

			/**
			 * Register matchMedia queries for main manu.
			 */
			registerMenuBreakpoints() {
				this.queryMenuMd = window.matchMedia('(min-width:600px)');
				this.queryMenuLg = window.matchMedia('(min-width:1100px)');

				this.queryMenuMd.addListener(this.setMenuVisibility);
				this.queryMenuLg.addListener(this.setMenuVisibility);

				this.setMenuVisibility();
			},


			/**
			 * Define the visible, open and collapsed properties
			 * of the main menu.
			 */
			setMenuVisibility() {
				this.$emit('closeMenuOverlay');
				this.isResizing = true;

				if (this.queryMenuLg.matches) {
					this.menuIsCollapsed = sessionStorage.getItem("menuCollapsed") === 'true';
					this.menuIsVisible = true;
					this.menuIsOpen = sessionStorage.getItem("menuCollapsed") !== 'true';
					this.screenSize = 'lg';
				}
				else if (this.queryMenuMd.matches) {
					this.menuIsCollapsed = true;
					this.menuIsVisible = true;
					this.menuIsOpen = false;
					this.screenSize = 'md';
				}
				else {
					this.menuIsCollapsed = false;
					this.menuIsVisible = false;
					this.menuIsOpen = false;
					this.screenSize = 'sm';
				}

				Vue.nextTick(() => this.isResizing = false);
			},

			/*
			* Return a new instance of FocusTrap for main menu.
			*/
			setMenuFocusTrap() {
				this.menuFocusTrap = window.FocusTrap(this.menu, {
					escapeDeactivates: false,
					clickOutsideDeactivates: true
				});

				this.menuFocusTrap.activate();
			},

			/**
			 * Remove the FocusTrap instance.
			 */
			destroyMenuFocusTrap() {
				if (this.menuFocusTrap) {
					this.menuFocusTrap.deactivate();
					this.menuFocusTrap = null;
				}
			}
		}
	});
})();
