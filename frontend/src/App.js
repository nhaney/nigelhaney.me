import React, { Component } from 'react';

import { BrowserRouter, Route, Switch } from 'react-router-dom';

import {CircleArrow as ScrollUpButton} from 'react-scroll-up-button';

import Container from 'react-bootstrap/Container';

import Navigation from './components/Navigation';
import BlogPreview from './components/blog/BlogPreview';
import BlogPost from './components/blog/BlogPost';
import AboutMe from './components/about/AboutMe';
import GamePreviewContainer from './components/games/GamePreviewContainer';
import LeaderboardContainer from './components/games/LeaderboardContainer';
import ExperienceContainer from './components/experience/ExperienceContainer';
import HomePage from './components/home/HomePage';
import Header from './components/Header';
import Footer from './components/Footer';
import NotFound from './components/NotFound';
import './App.css';

class App extends Component {
	render() {
		// console.log(this.state.banner_items);
		return (
			<BrowserRouter>
				<div className="main-container">
					<Header />
					<Navigation />
					<Switch>
						<Route path="/" exact component={HomePage} />
						<Route path="/blog" exact>
							<Container>
								<h1 style={{textAlign:"center"}}><b>Nigel's Blog</b></h1>
								<hr />
								<BlogPreview />
							</Container>
						</Route>
						<Route path="/blog/:post_title" component={BlogPost} />
						<Route path="/about">
							<AboutMe />
						</Route>
						<Route exact path="/games" component={GamePreviewContainer} />
						<Route exact path="/games/scores/:game_name" component={LeaderboardContainer} />
						<Route path="/experience" component={ExperienceContainer} />
						<Route component={NotFound} />
					</Switch>
					<Footer />
					<ScrollUpButton ContainerClassName="scrollbutton" TransitionClassName="scrollbutton"/>
				</div>
			</BrowserRouter>
		);
	}
}

export default App;


